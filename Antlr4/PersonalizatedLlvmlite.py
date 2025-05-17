from llvmlite import ir
from llvmlite.ir import Constant, IRBuilder
import llvmlite.binding as llvm

class LLVMGenerator:
    def __init__(self):
        # Initialize LLVM
        llvm.initialize()
        llvm.initialize_native_target()
        llvm.initialize_native_asmprinter()
        self.symbol_table_stack = [{}]
        # Create module
        self.module = ir.Module(name="main_module")
        self.module.triple = llvm.get_process_triple()
        target = llvm.Target.from_triple(self.module.triple)
        self.module.data_layout = target.create_target_machine().target_data
        
        # Initialize builder and context
        self.builder = None
        self.current_function = None
        
        # Symbol tables
        self.functions = {}
        self.symbol_table = {}
        self.string_constants = {}
        
        # Type definitions
        self.int_type = ir.IntType(32)       # entero
        self.double_type = ir.DoubleType()   # decimal
        self.bool_type = ir.IntType(1)       # bool
        self.void_type = ir.VoidType()       # void
        self.char_ptr_type = ir.IntType(8).as_pointer()  # cadena
        
        # Initialize builtins
        self._declare_builtins()
    def _enter_scope(self):
        """Entrar a un nuevo scope"""
        self.symbol_table_stack.append({'_strings': {}})

    def _current_symbol_table(self):
        """Obtener la tabla de símbolos actual"""
        return self.symbol_table_stack[-1]
        

    def _exit_scope(self):
        """Salir del scope actual"""
        if len(self.symbol_table_stack) > 1:
            self.symbol_table_stack.pop()
            

    def _declare_builtins(self):
        """Declare built-in functions like printf"""
        printf_type = ir.FunctionType(self.int_type, [self.char_ptr_type], var_arg=True)
        ir.Function(self.module, printf_type, name="printf")

    def generate_code(self, ast_node):
        """Generate LLVM IR from AST"""
        # Create main function
        main_func_type = ir.FunctionType(self.int_type, [])
        main_func = ir.Function(self.module, main_func_type, name="main")
        self.current_function = main_func
        
        # Create entry block
        entry_block = main_func.append_basic_block(name="entry")
        self.builder = IRBuilder(entry_block)
        
        # Generate code for the AST
        self._generate_node(ast_node)
        
        # Ensure main has a return at the end
        if not self.builder.block.is_terminated:
            self.builder.ret(Constant(self.int_type, 0))
        
        return self.module


    def _generate_node(self, node):
        """Dispatch node generation based on type"""
        node_type = node.type
        
        if node_type == "Program":
            for child in node.children:
                self._generate_node(child)
                
        elif node_type == "MainFunction":
            for child in node.children:
                self._generate_node(child)
                
        elif node_type == "Block":
            for child in node.children:
                self._generate_node(child)
                
        elif node_type == "VariableDecl":
            self._generate_variable_decl(node)
                
        elif node_type == "Assignment":
            self._generate_assignment(node)
            
        elif node_type == "PrintStatement":
            self._generate_print(node.children[0])
            
        elif node_type == "IfStatement":
            self._generate_if_statement(node)
            
        elif node_type == "WhileLoop":
            self._generate_while_loop(node)
            
        elif node_type == "ForLoop":
            self._generate_for_loop(node)
            
        elif node_type == "FunctionDecl":
            self._generate_function_decl(node)
            
        elif node_type == "FunctionCall":
            return self._generate_function_call(node)
            
        elif node_type == "ReturnStatement":
            self._generate_return(node)

    def _generate_variable_decl(self, node):
        """Generate variable declaration"""
        var_name = node.value
        var_type = self._llvm_type(node.children[0].value)
        
        # Allocate space on stack
        ptr = self.builder.alloca(var_type, name=var_name)
        self._current_symbol_table()[var_name] = ptr
        
        # Initialize if needed
        if len(node.children) > 1:
            value = self._generate_expression(node.children[1])
            # Handle string type conversion
            if isinstance(value.type, ir.PointerType) and isinstance(value.type.pointee, ir.ArrayType):
                if var_type == self.char_ptr_type:
                    # Convert array pointer to char pointer
                    zero = Constant(ir.IntType(32), 0)
                    value = self.builder.gep(value, [zero, zero], name=f"{var_name}_ptr_cast")
            self.builder.store(value, ptr)
            
    def _generate_assignment(self, node):
        """Generate variable assignment"""
        var_name = node.value
        # Buscar la variable en todos los scopes
        for scope in reversed(self.symbol_table_stack):
            if var_name in scope:
                ptr = scope[var_name]
                value = self._generate_expression(node.children[0])
                self.builder.store(value, ptr)
                return
        raise Exception(f"Variable '{var_name}' no declarada")

    def _generate_print(self, expr_node):
        """Generate print statement"""
        value = self._generate_expression(expr_node)
        value_type = self._get_expression_type(expr_node)
        
        # Get printf function
        printf = self.module.get_global("printf")
        
        # Create format string based on type
        if isinstance(value_type, ir.IntType) and value_type.width == 32:
            fmt_str = "%d\n\0"
        elif isinstance(value_type, ir.DoubleType):
            fmt_str = "%f\n\0"
        elif isinstance(value_type, ir.IntType) and value_type.width == 1:  # bool
            fmt_str = "%d\n\0"
        else:  # string
            fmt_str = "%s\n\0"
        
        # Create global constant for format string
        if fmt_str not in self.string_constants:
            byte_array = bytearray(fmt_str.encode("utf8"))
            fmt = ir.Constant(ir.ArrayType(ir.IntType(8), len(byte_array)), byte_array)
            global_fmt = ir.GlobalVariable(self.module, fmt.type, name=f"fmt.{len(self.string_constants)}")
            global_fmt.linkage = "internal"
            global_fmt.global_constant = True
            global_fmt.initializer = fmt
            self.string_constants[fmt_str] = global_fmt
        
        # Get pointer to format string
        fmt_ptr = self.builder.bitcast(self.string_constants[fmt_str], self.char_ptr_type)
        
        # Call printf
        if isinstance(value_type, ir.IntType) and value_type.width == 1:  # bool
            value = self.builder.zext(value, self.int_type)
        self.builder.call(printf, [fmt_ptr, value])

    def _generate_if_statement(self, node):
        """Generate if-else statement"""
        condition = node.children[0]
        then_block_node = node.children[1]
        else_block_node = node.children[2] if len(node.children) > 2 else None

        # Crear bloques básicos
        then_block = self.builder.append_basic_block("if.then")
        end_block = self.builder.append_basic_block("if.end")
        else_block = self.builder.append_basic_block("if.else") if else_block_node else end_block

        # Evaluar condición
        cond_value = self._generate_expression(condition)

        # Asegurar que cond_value sea de tipo i1
        if cond_value.type != self.bool_type:
            cond_value = self.builder.icmp_unsigned("!=", cond_value, ir.Constant(cond_value.type, 0))

        self.builder.cbranch(cond_value, then_block, else_block)

        # Generar bloque "then"
        self.builder.position_at_end(then_block)
        self._generate_node(then_block_node)
        if not self.builder.block.is_terminated:
            self.builder.branch(end_block)

        # Generar bloque "else" si existe
        if else_block_node and else_block != end_block:
            self.builder.position_at_end(else_block)
            self._generate_node(else_block_node)
            if not self.builder.block.is_terminated:
                self.builder.branch(end_block)

        # Solo posicionarse en end_block si no estamos ya allí
        if self.builder.block != end_block:
            self.builder.position_at_end(end_block)
            
    def _generate_while_loop(self, node):
        condition = node.children[0]
        body = node.children[1]

        # Guardar el bloque actual para volver después del bucle
        current_block = self.builder.block

        cond_block = self.builder.append_basic_block("while.cond")
        body_block = self.builder.append_basic_block("while.body")
        end_block = self.builder.append_basic_block("while.end")

        # Saltar al bloque de condición
        self.builder.branch(cond_block)

        # Bloque de condición
        self.builder.position_at_end(cond_block)
        cond_value = self._generate_expression(condition)

        if cond_value.type != self.bool_type:
            cond_value = self.builder.icmp_unsigned("!=", cond_value, ir.Constant(cond_value.type, 0))

        self.builder.cbranch(cond_value, body_block, end_block)

        # Bloque del cuerpo
        self.builder.position_at_end(body_block)
        self._generate_node(body)
        if not self.builder.block.is_terminated:
            self.builder.branch(cond_block)

        # Posicionarse en el bloque final
        self.builder.position_at_end(end_block)

    def _generate_for_loop(self, node):
        init, cond, update, body = node.children
        self._enter_scope()

        # Guardar el bloque actual
        current_block = self.builder.block

        cond_block = self.builder.append_basic_block("for.cond")
        body_block = self.builder.append_basic_block("for.body")
        update_block = self.builder.append_basic_block("for.update")
        end_block = self.builder.append_basic_block("for.end")

        # Generar código de inicialización
        self._generate_node(init)
        self.builder.branch(cond_block)

        # Bloque de condición
        self.builder.position_at_end(cond_block)
        cond_value = self._generate_expression(cond)
        if cond_value.type != self.bool_type:
            cond_value = self.builder.icmp_unsigned("!=", cond_value, ir.Constant(cond_value.type, 0))
        self.builder.cbranch(cond_value, body_block, end_block)

        # Bloque del cuerpo
        self.builder.position_at_end(body_block)
        self._generate_node(body)
        if not self.builder.block.is_terminated:
            self.builder.branch(update_block)

        # Bloque de actualización
        self.builder.position_at_end(update_block)
        self._generate_node(update)
        if not self.builder.block.is_terminated:
            self.builder.branch(cond_block)

        # Posicionarse en el bloque final
        self.builder.position_at_end(end_block)
        self._exit_scope()
        
    def _generate_function_decl(self, node):
        """Generate function declaration with proper scope handling"""
        func_name = node.value
        return_type = self._llvm_type(node.children[0].value)
        params = node.children[1].children
        body_node = node.children[2]

        # Registrar la función primero (importante para recursión)
        param_types = [self._llvm_type(p.children[0].value) for p in params]
        func_type = ir.FunctionType(return_type, param_types)
        func = ir.Function(self.module, func_type, name=func_name)
        
        # Guardar información de la función antes de generar el cuerpo
        self.functions[func_name] = {
            'function': func,
            'return_type': return_type
        }

        # 1. Backup current context
        old_context = {
            'function': self.current_function,
            'builder': self.builder,
            'symbol_table_stack': self.symbol_table_stack.copy(),
            'functions': self.functions.copy()
        }

        # 2. Set new context for function body
        self.current_function = func
        self.symbol_table_stack = [{}]  # reset to global scope
        entry_block = func.append_basic_block("entry")
        self.builder = IRBuilder(entry_block)

        # 3. New scope for parameters
        self._enter_scope()

        # 4. Handle parameters
        for i, (param, param_node) in enumerate(zip(func.args, params)):
            param_name = param_node.value
            ptr = self.builder.alloca(param.type, name=f"{param_name}.addr")
            self.builder.store(param, ptr)
            self._current_symbol_table()[param_name] = ptr

        # 5. Generate function body
        self._generate_node(body_node)

        # 6. Ensure function has a proper termination
        if not self.builder.block.is_terminated:
            if isinstance(return_type, ir.VoidType):
                self.builder.ret_void()
            else:
                # For non-void functions, return a default value
                if return_type == self.int_type:
                    self.builder.ret(Constant(self.int_type, 0))
                elif return_type == self.double_type:
                    self.builder.ret(Constant(self.double_type, 0.0))
                elif return_type == self.bool_type:
                    self.builder.ret(Constant(self.bool_type, False))
                else:
                    self.builder.ret_void()

        # 7. Restore old context
        self.current_function = old_context['function']
        self.builder = old_context['builder']
        self.symbol_table_stack = old_context['symbol_table_stack']
        self.functions = old_context['functions']
    def _generate_function_call(self, node):
        """Generar llamada a función"""
        func_name = node.value
        args = [self._generate_expression(child) for child in node.children]

        if func_name not in self.functions:
            raise Exception(f"Función '{func_name}' no declarada")

        func_info = self.functions[func_name]
        func = func_info['function']

        if not isinstance(func, ir.Function):
            raise Exception(f"'{func_name}' no es una función válida")

        # Generar la llamada y devolver el valor
        call = self.builder.call(func, args, name=f"call_{func_name}")
        return call  # Asegurarse de devolver el valor de la llamada


    def _generate_return(self, node):
        """Generate return statement"""
        if not self.current_function:
            raise Exception("Return statement outside of function")
        
        # Obtener el tipo de retorno de la función actual
        return_type = self.current_function.function_type.return_type
        
        if len(node.children) > 0:
            ret_value = self._generate_expression(node.children[0])
            # Asegurarse de que el tipo de retorno coincida con la función
            if ret_value.type != return_type:
                if isinstance(ret_value.type, ir.IntType) and isinstance(return_type, ir.DoubleType):
                    ret_value = self.builder.sitofp(ret_value, self.double_type)
                elif isinstance(ret_value.type, ir.DoubleType) and isinstance(return_type, ir.IntType):
                    ret_value = self.builder.fptosi(ret_value, self.int_type)
            self.builder.ret(ret_value)
        else:
            if isinstance(return_type, ir.VoidType):
                self.builder.ret_void()
            else:
                # Retornar cero por defecto para tipos no void
                zero_val = ir.Constant(return_type, 0)
                self.builder.ret(zero_val)

    def _generate_expression(self, node):
        """Generate expression code"""
        if node.type == "Literal":
            return self._generate_literal(node)
        elif node.type == "Variable":
            return self._generate_variable(node)
        elif node.type == "BinaryOp":
            return self._generate_binary_op(node)
        elif node.type == "UnaryOp":
            return self._generate_unary_op(node)
        elif node.type == "FunctionCall":
            return self._generate_function_call(node)
        else:
            return Constant(self.int_type, 0)  # Default value

    def _generate_literal(self, node):
        """Generate literal value"""
        if isinstance(node.value, bool):
            return Constant(self.bool_type, int(node.value))
        elif isinstance(node.value, int):
            return Constant(self.int_type, node.value)
        elif isinstance(node.value, float):
            return Constant(self.double_type, node.value)
        elif isinstance(node.value, str):
            return self._generate_string(node.value)
        else:
            return Constant(self.int_type, 0)

    def _generate_string(self, value):
        # Verificar si ya tenemos esta cadena en el scope actual
        for scope in reversed(self.symbol_table_stack):
            if value in scope.get('_strings', {}):
                return scope['_strings'][value]
        
        # Crear constante de cadena
        str_type = ir.ArrayType(ir.IntType(8), len(value) + 1)
        str_const = ir.Constant(str_type, bytearray(value.encode('utf-8') + b'\x00'))
        
        # Generar nombre único considerando el scope
        scope_depth = len(self.symbol_table_stack)
        str_name = f"str.{scope_depth}.{len(self.string_constants)}"
        
        # Crear variable global
        global_str = ir.GlobalVariable(self.module, str_type, name=str_name)
        global_str.linkage = "internal"
        global_str.global_constant = True
        global_str.initializer = str_const
        
        # Registrar en el scope actual y en el registro global
        if '_strings' not in self._current_symbol_table():
            self._current_symbol_table()['_strings'] = {}
        self._current_symbol_table()['_strings'][value] = global_str
        self.string_constants[value] = global_str
        
        # Obtener puntero al primer carácter (como i8*)
        zero = Constant(ir.IntType(32), 0)
        return self.builder.gep(global_str, [zero, zero], name=f"{str_name}_ptr")

    def _generate_variable(self, node):
        """Generate variable access"""
        var_name = node.value
        # Buscar la variable en todos los scopes, desde el más interno
        for scope in reversed(self.symbol_table_stack):
            if var_name in scope:
                ptr = scope[var_name]
                return self.builder.load(ptr, name=f"{var_name}.val")
        raise Exception(f"Variable '{var_name}' no declarada")
    
    def _generate_binary_op(self, node):
        """Generate binary operation"""
        left = self._generate_expression(node.children[0])
        right = self._generate_expression(node.children[1])
        op = node.value
        
        # Determine types
        left_type = self._get_expression_type(node.children[0])
        right_type = self._get_expression_type(node.children[1])
        
        # Convert types if needed
        if left_type != right_type:
            if isinstance(left_type, ir.IntType) and isinstance(right_type, ir.DoubleType):
                left = self.builder.sitofp(left, self.double_type)
            elif isinstance(left_type, ir.DoubleType) and isinstance(right_type, ir.IntType):
                right = self.builder.sitofp(right, self.double_type)
        
        # Perform operation
        if op in ["+", "-", "*", "/"]:
            if isinstance(left_type, ir.DoubleType) or isinstance(right_type, ir.DoubleType):
                if op == "+": 
                    return self.builder.fadd(left, right, name="addtmp")
                elif op == "-": 
                    return self.builder.fsub(left, right, name="subtmp")
                elif op == "*": 
                    return self.builder.fmul(left, right, name="multmp")
                else: 
                    return self.builder.fdiv(left, right, name="divtmp")
            else:
                if op == "+": 
                    return self.builder.add(left, right, name="addtmp")
                elif op == "-": 
                    return self.builder.sub(left, right, name="subtmp")
                elif op == "*": 
                    return self.builder.mul(left, right, name="multmp")
                else: 
                    return self.builder.sdiv(left, right, name="divtmp")
        elif op in ["<", ">", "<=", ">=", "==", "!="]:
            if isinstance(left_type, ir.DoubleType) or isinstance(right_type, ir.DoubleType):
                if op == "<": 
                    return self.builder.fcmp_ordered("<", left, right, name="cmptmp")
                elif op == ">": 
                    return self.builder.fcmp_ordered(">", left, right, name="cmptmp")
                elif op == "<=": 
                    return self.builder.fcmp_ordered("<=", left, right, name="cmptmp")
                elif op == ">=": 
                    return self.builder.fcmp_ordered(">=", left, right, name="cmptmp")
                elif op == "==": 
                    return self.builder.fcmp_ordered("==", left, right, name="cmptmp")
                else: 
                    return self.builder.fcmp_ordered("!=", left, right, name="cmptmp")
            else:
                if op == "<": 
                    return self.builder.icmp_signed("<", left, right, name="cmptmp")
                elif op == ">": 
                    return self.builder.icmp_signed(">", left, right, name="cmptmp")
                elif op == "<=": 
                    return self.builder.icmp_signed("<=", left, right, name="cmptmp")
                elif op == ">=": 
                    return self.builder.icmp_signed(">=", left, right, name="cmptmp")
                elif op == "==": 
                    return self.builder.icmp_signed("==", left, right, name="cmptmp")
                else: 
                    return self.builder.icmp_signed("!=", left, right, name="cmptmp")
    def _generate_unary_op(self, node):
        """Generate unary operation"""
        operand = self._generate_expression(node.children[0])
        op = node.value
        
        if op == "-":
            if isinstance(operand.type, ir.DoubleType):
                return self.builder.fneg(operand)
            else:
                return self.builder.sub(Constant(operand.type, 0), operand)
        elif op in ["++", "--"]:
            # Handle increment/decrement
            var_name = node.children[0].value
            ptr = self.symbol_table[var_name]
            value = self.builder.load(ptr)
            
            if isinstance(value.type, ir.DoubleType):
                delta = Constant(value.type, 1.0 if op == "++" else -1.0)
                new_value = self.builder.fadd(value, delta)
            else:
                delta = Constant(value.type, 1 if op == "++" else -1)
                new_value = self.builder.add(value, delta)
            
            self.builder.store(new_value, ptr)
            return new_value

    def _llvm_type(self, type_str):
        """Map language type to LLVM type"""
        type_map = {
            "entero": self.int_type,
            "decimal": self.double_type,
            "cadena": self.char_ptr_type,
            "bool": self.bool_type,
            "void": self.void_type
        }
        return type_map.get(type_str, self.int_type)

    def _get_expression_type(self, node):
        """Get LLVM type of an expression"""
        if node.type == "Literal":
            if isinstance(node.value, bool):
                return self.bool_type
            elif isinstance(node.value, int):
                return self.int_type
            elif isinstance(node.value, float):
                return self.double_type
            elif isinstance(node.value, str):
                return self.char_ptr_type
        elif node.type == "Variable":
            # Buscar la variable en todos los scopes
            for scope in reversed(self.symbol_table_stack):
                if node.value in scope:
                    ptr = scope[node.value]
                    return ptr.type.pointee
            raise Exception(f"Variable '{node.value}' no declarada")
        elif node.type == "BinaryOp":
            left_type = self._get_expression_type(node.children[0])
            right_type = self._get_expression_type(node.children[1])
            
            if node.value in ["+", "-", "*", "/"]:
                if isinstance(left_type, ir.DoubleType) or isinstance(right_type, ir.DoubleType):
                    return self.double_type
                return self.int_type
            else:
                return self.bool_type
        elif node.type == "UnaryOp":
            return self._get_expression_type(node.children[0])
        elif node.type == "FunctionCall":
            if node.value in self.functions:
                return self.functions[node.value]['return_type']
            return self.int_type
        
        return self.int_type

    def save_to_file(self, filename="output.ll"):
        """Save generated IR to file"""
        llvm_ir = str(self.module)
        with open(filename, 'w') as f:
            f.write(llvm_ir)
        print(f"LLVM IR saved to {filename}")