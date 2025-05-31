from llvmlite import ir, binding as llvm

class LLVMGenerator:
    def __init__(self, windows_target=False):
        llvm.initialize()
        llvm.initialize_native_target()
        llvm.initialize_native_asmprinter()
        self.module = ir.Module(name="main_module")
        # Establecer triple y datalayout válidos según el destino
        if windows_target:
            self.module.triple = "x86_64-w64-windows-gnu"
            # Data layout para Windows x86_64 (puede requerir ajuste según tu toolchain)
            self.module.data_layout = "e-m:w-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
        else:
            self.module.triple = llvm.get_default_triple()
            target = llvm.Target.from_default_triple()
            target_machine = target.create_target_machine()
            self.module.data_layout = target_machine.target_data
        self.builder = None
        self.current_function = None
        self.symbol_table_stack = [{}]  # Pila de scopes
        self.functions = {}
        self.string_constants = {}
        self.int_type = ir.IntType(32)
        self.double_type = ir.DoubleType()
        self.bool_type = ir.IntType(1)
        self.void_type = ir.VoidType()
        self.char_ptr_type = ir.IntType(8).as_pointer()
        self._declare_builtins()

    def _declare_builtins(self):
        printf_ty = ir.FunctionType(self.int_type, [self.char_ptr_type], var_arg=True)
        self.functions["printf"] = ir.Function(self.module, printf_ty, name="printf")

    def _enter_scope(self):
        self.symbol_table_stack.append({})

    def _exit_scope(self):
        self.symbol_table_stack.pop()

    def _current_symbol_table(self):
        return self.symbol_table_stack[-1]

    def generate_code(self, ast):
        main_ty = ir.FunctionType(self.int_type, [])
        main_fn = ir.Function(self.module, main_ty, name="main")
        self.current_function = main_fn
        block = main_fn.append_basic_block("entry")
        self.builder = ir.IRBuilder(block)
        self._generate_node(ast)
        if not self.builder.block.is_terminated:
            self.builder.ret(ir.Constant(self.int_type, 0))
        return self.module

    def _generate_node(self, node):
        if node.type == "Program":
            for child in node.children:
                self._generate_node(child)
        elif node.type == "MainFunction":
            self._enter_scope()
            for child in node.children:
                self._generate_node(child)
            self._exit_scope()
        elif node.type == "Block":
            self._enter_scope()
            for stmt in node.children:
                self._generate_node(stmt)
            self._exit_scope()
        elif node.type == "VariableDecl":
            self._generate_variable_decl(node)
        elif node.type == "Assignment":
            self._generate_assignment(node)
        elif node.type == "PrintStatement":
            self._generate_print(node.children[0])
        elif node.type == "IfStatement":
            self._generate_if(node)
        elif node.type == "WhileLoop":
            self._generate_while(node)
        elif node.type == "ForLoop":
            self._generate_for(node)
        elif node.type == "FunctionDecl":
            self._generate_function_decl(node)
        elif node.type == "FunctionCall":
            self._generate_function_call(node)
        elif node.type == "ReturnStatement":
            self._generate_return(node)
        # ...otros nodos...

    def _generate_variable_decl(self, node):
        var_name = node.value
        var_type = self._llvm_type(node.children[0].value)
        ptr = self.builder.alloca(var_type, name=var_name)
        self._current_symbol_table()[var_name] = ptr
        if len(node.children) > 1:
            value = self._generate_expression(node.children[1])
            self.builder.store(value, ptr)

    def _generate_assignment(self, node):
        var_name = node.value
        value = self._generate_expression(node.children[0])
        for scope in reversed(self.symbol_table_stack):
            if var_name in scope:
                self.builder.store(value, scope[var_name])
                return
        raise NameError(f"Variable '{var_name}' no declarada")

    def _generate_print(self, expr_node):
        value = self._generate_expression(expr_node)
        value_type = value.type
        if isinstance(value_type, ir.IntType) and value_type.width == 32:
            fmt = "%d\\0a\\00"
        elif isinstance(value_type, ir.DoubleType):
            fmt = "%f\\0a\\00"
        else:
            fmt = "%d\\0a\\00"
        if fmt not in self.string_constants:
            c_fmt = ir.GlobalVariable(self.module, ir.ArrayType(ir.IntType(8), len(fmt)), name=f"fmt_{len(self.string_constants)}")
            c_fmt.linkage = "internal"
            c_fmt.global_constant = True
            c_fmt.initializer = ir.Constant(ir.ArrayType(ir.IntType(8), len(fmt)), bytearray(fmt.encode("utf8")))
            self.string_constants[fmt] = c_fmt
        fmt_ptr = self.builder.bitcast(self.string_constants[fmt], self.char_ptr_type)
        self.builder.call(self.functions["printf"], [fmt_ptr, value])

    def _generate_if(self, node):
        cond = self._generate_expression(node.children[0].children[0])
        then_block = self.current_function.append_basic_block("if.then")
        end_block = self.current_function.append_basic_block("if.end")
        self.builder.cbranch(cond, then_block, end_block)
        self.builder.position_at_end(then_block)
        self._generate_node(node.children[1].children[0])
        if not self.builder.block.is_terminated:
            self.builder.branch(end_block)
        self.builder.position_at_end(end_block)

    def _generate_while(self, node):
        cond_block = self.current_function.append_basic_block("while.cond")
        body_block = self.current_function.append_basic_block("while.body")
        end_block = self.current_function.append_basic_block("while.end")
        self.builder.branch(cond_block)
        self.builder.position_at_end(cond_block)
        cond = self._generate_expression(node.children[0])
        self.builder.cbranch(cond, body_block, end_block)
        self.builder.position_at_end(body_block)
        self._generate_node(node.children[1])
        if not self.builder.block.is_terminated:
            self.builder.branch(cond_block)
        self.builder.position_at_end(end_block)

    def _generate_for(self, node):
        self._enter_scope()
        self._generate_node(node.children[0])  # init
        cond_block = self.current_function.append_basic_block("for.cond")
        body_block = self.current_function.append_basic_block("for.body")
        update_block = self.current_function.append_basic_block("for.update")
        end_block = self.current_function.append_basic_block("for.end")
        self.builder.branch(cond_block)
        self.builder.position_at_end(cond_block)
        cond = self._generate_expression(node.children[1])
        self.builder.cbranch(cond, body_block, end_block)
        self.builder.position_at_end(body_block)
        self._generate_node(node.children[3])  # body
        if not self.builder.block.is_terminated:
            self.builder.branch(update_block)
        self.builder.position_at_end(update_block)
        update_node = node.children[2]
        if update_node.type in ("Assignment", "UnaryOp"):
            self._generate_expression(update_node)
        else:
            self._generate_node(update_node)
        self.builder.branch(cond_block)
        self.builder.position_at_end(end_block)
        self._exit_scope()

    def _generate_function_decl(self, node):
        name = node.value
        ret_type = self._llvm_type(node.children[0].value)
        params = node.children[1].children
        param_types = [self._llvm_type(p.children[0].value) for p in params]
        func_ty = ir.FunctionType(ret_type, param_types)
        func = ir.Function(self.module, func_ty, name=name)
        self.functions[name] = func
        self._enter_scope()
        for i, p in enumerate(params):
            ptr = self.builder.alloca(param_types[i], name=p.value)
            self.builder.store(func.args[i], ptr)
            self._current_symbol_table()[p.value] = ptr
        block = func.append_basic_block("entry")
        old_builder = self.builder
        self.builder = ir.IRBuilder(block)
        for child in node.children[2:]:
            self._generate_node(child)
        if not self.builder.block.is_terminated:
            if isinstance(ret_type, ir.VoidType):
                self.builder.ret_void()
            else:
                self.builder.ret(ir.Constant(ret_type, 0))
        self.builder = old_builder
        self._exit_scope()

    def _generate_function_call(self, node):
        func = self.functions[node.value]
        args = [self._generate_expression(arg) for arg in node.children]
        return self.builder.call(func, args)

    def _generate_return(self, node):
        value = self._generate_expression(node.children[0])
        self.builder.ret(value)

    def _generate_expression(self, node):
        if node.type == "Literal":
            return self._generate_literal(node)
        elif node.type == "Variable":
            for scope in reversed(self.symbol_table_stack):
                if node.value in scope:
                    return self.builder.load(scope[node.value], name=f"{node.value}.val")
            raise NameError(f"Variable '{node.value}' no declarada")
        elif node.type == "BinaryOp":
            # Soporte para operadores lógicos y aritméticos
            left = self._generate_expression(node.children[0])
            right = self._generate_expression(node.children[1])
            op = node.value
            if op == "&&":
                return self.builder.and_(left, right, name="andtmp")
            elif op == "||":
                return self.builder.or_(left, right, name="ortmp")
            elif op == "%":
                return self.builder.srem(left, right, name="modtmp")
            else:
                return self._generate_binary_op(node)
        elif node.type == "UnaryOp":
            return self._generate_unary_op(node)
        elif node.type == "FunctionCall":
            return self._generate_function_call(node)
        # ...otros tipos...
        else:
            raise ValueError(f"Tipo de expresión no soportado: {node.type}")

    def _generate_literal(self, node):
        v = node.value
        if isinstance(v, bool):
            return ir.Constant(self.bool_type, int(v))
        elif isinstance(v, int):
            return ir.Constant(self.int_type, v)
        elif isinstance(v, float):
            return ir.Constant(self.double_type, v)
        else:
            raise ValueError("Tipo literal no soportado")

    def _generate_binary_op(self, node):
        left = self._generate_expression(node.children[0])
        right = self._generate_expression(node.children[1])
        op = node.value
        # Distinguir tipos
        if isinstance(left.type, ir.DoubleType) or isinstance(right.type, ir.DoubleType):
            # Promocionar a double si es necesario
            if isinstance(left.type, ir.IntType):
                left = self.builder.sitofp(left, self.double_type)
            if isinstance(right.type, ir.IntType):
                right = self.builder.sitofp(right, self.double_type)
            if op == "+":
                return self.builder.fadd(left, right, name="addtmp")
            elif op == "-":
                return self.builder.fsub(left, right, name="subtmp")
            elif op == "*":
                return self.builder.fmul(left, right, name="multmp")
            elif op == "/":
                return self.builder.fdiv(left, right, name="divtmp")
            elif op == "<":
                return self.builder.fcmp_ordered("<", left, right, name="cmptmp")
            elif op == ">":
                return self.builder.fcmp_ordered(">", left, right, name="cmptmp")
            elif op == "<=":
                return self.builder.fcmp_ordered("<=", left, right, name="cmptmp")
            elif op == ">=":
                return self.builder.fcmp_ordered(">=", left, right, name="cmptmp")
            elif op == "==":
                return self.builder.fcmp_ordered("==", left, right, name="cmptmp")
            elif op == "!=":
                return self.builder.fcmp_ordered("!=", left, right, name="cmptmp")
            else:
                raise ValueError(f"Operador binario no soportado para decimales: {op}")
        else:
            if op == "+":
                return self.builder.add(left, right, name="addtmp")
            elif op == "-":
                return self.builder.sub(left, right, name="subtmp")
            elif op == "*":
                return self.builder.mul(left, right, name="multmp")
            elif op == "/":
                return self.builder.sdiv(left, right, name="divtmp")
            elif op == "%":
                return self.builder.srem(left, right, name="modtmp")
            elif op == "<":
                return self.builder.icmp_signed("<", left, right, name="cmptmp")
            elif op == ">":
                return self.builder.icmp_signed(">", left, right, name="cmptmp")
            elif op == "<=":
                return self.builder.icmp_signed("<=", left, right, name="cmptmp")
            elif op == ">=":
                return self.builder.icmp_signed(">=", left, right, name="cmptmp")
            elif op == "==":
                return self.builder.icmp_signed("==", left, right, name="cmptmp")
            elif op == "!=":
                return self.builder.icmp_signed("!=", left, right, name="cmptmp")
            else:
                raise ValueError(f"Operador binario no soportado para enteros: {op}")

    def _generate_unary_op(self, node):
        operand = self._generate_expression(node.children[0])
        if node.value == "-":
            return self.builder.neg(operand, name="negtmp")
        elif node.value == "raiz":
            # Implementa sqrt si lo necesitas
            pass
        elif node.value == "++":
            var_name = node.children[0].value
            for scope in reversed(self.symbol_table_stack):
                if var_name in scope:
                    ptr = scope[var_name]
                    val = self.builder.load(ptr)
                    new_val = self.builder.add(val, ir.Constant(self.int_type, 1))
                    self.builder.store(new_val, ptr)
                    return new_val
        elif node.value == "--":
            # Pre-decremento
            var_name = node.children[0].value
            for scope in reversed(self.symbol_table_stack):
                if var_name in scope:
                    ptr = scope[var_name]
                    val = self.builder.load(ptr)
                    new_val = self.builder.sub(val, ir.Constant(self.int_type, 1))
                    self.builder.store(new_val, ptr)
                    return new_val
        else:
            raise ValueError(f"Operador unario no soportado: {node.value}")

    def _llvm_type(self, type_str):
        if type_str == "entero":
            return self.int_type
        elif type_str == "decimal":
            return self.double_type
        elif type_str == "bool":
            return self.bool_type
        elif type_str == "void":
            return self.void_type
        else:
            raise ValueError(f"Tipo no soportado: {type_str}")

    def save_to_file(self, filename="output.ll"):
        with open(filename, "w") as f:
            f.write(str(self.module))