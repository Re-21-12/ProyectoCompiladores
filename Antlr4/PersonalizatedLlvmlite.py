from llvmlite import ir
from llvmlite.ir import Constant, IRBuilder
import llvmlite.binding as llvm

class LLVMGenerator:
    def __init__(self):
        llvm.initialize()
        llvm.initialize_native_target()
        llvm.initialize_native_asmprinter()
        
        # Módulo LLVM con información de target
        self.module = ir.Module(name="main_module")
        self.module.triple = llvm.get_process_triple()
        target = llvm.Target.from_triple(self.module.triple)
        
        # CORRECT WAY to get data layout:
        self.module.data_layout = target.create_target_machine().target_data
        
        self.builder = None
        self.current_function = None
        
        # Resto de la inicialización...
        self.functions = {}
        self.symbol_table = {}
        self.string_constants = {}
        self.label_count = 0
        self.var_count = 0
        
        # Configuración básica de tipos
        self.int_type = ir.IntType(32)
        self.double_type = ir.DoubleType()
        self.void_type = ir.VoidType()
        self.bool_type = ir.IntType(1)
        self.char_ptr_type = ir.IntType(8).as_pointer()
        
        self.output = []
        self.indent = "  "

        self._declare_builtins()
        
    def _declare_builtins(self):
        """Declara funciones built-in como printf"""
        # Verificar si printf ya existe
        try:
            self.module.get_global("printf")
        except KeyError:
            # printf no existe, declararlo
            printf_ty = ir.FunctionType(self.int_type, [self.char_ptr_type], var_arg=True)
            ir.Function(self.module, printf_ty, name="printf")
        
    def generate_label(self, prefix="label"):
        self.label_count += 1
        return f"{prefix}_{self.label_count}"

    def generate_var(self, prefix="var"):
        self.var_count += 1
        return f"{prefix}_{self.var_count}"

    def _verify_module(self):
        """Verify the module structure is correct"""
        try:
            llvm.parse_assembly(str(self.module))
            print("Module verification passed")
        except Exception as e:
            print(f"Module verification failed: {str(e)}")
            # Print the problematic IR
            print("\nProblematic IR:")
            print(str(self.module))
            raise

    def generate_code(self, ast_node):
        main_func_type = ir.FunctionType(self.int_type, [])
        main_func = ir.Function(self.module, main_func_type, name="main")
        self.current_function = main_func  # Store the function object
        main_block = main_func.append_basic_block(name="entry")
        self.builder = IRBuilder(main_block)
        
        self._generate_node(ast_node)
        
        # Ensure main always returns a value
        if not main_block.is_terminated:
            self.builder.ret(Constant(self.int_type, 0))
        
        return self.module

    def _generate_node(self, node):
        """Genera código LLVM para un nodo del AST usando llvmlite"""
        node_type = node.type
        
        if node_type == "Program":
            for child in node.children:
                self._generate_node(child)
                
        elif node_type == "MainFunction":
            # El bloque main ya fue creado en generate_code()
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
        """Genera declaración de variable"""
        var_name = node.value
        var_type = self._llvm_type(node.children[0].value)
        
        # Asignar espacio en el stack
        ptr = self.builder.alloca(var_type, name=var_name)
        self.symbol_table[var_name] = ptr
        
        # Inicialización si existe
        if len(node.children) > 1:
            value = self._generate_expression(node.children[1])
            self.builder.store(value, ptr)

    def _generate_assignment(self, node):
        """Genera asignación de variable"""
        var_name = node.value
        ptr = self.symbol_table[var_name]
        value = self._generate_expression(node.children[0])
        self.builder.store(value, ptr)

    def declare_function(self, name, return_type, param_types):
        """Declara una función en el módulo LLVM"""
        # Convierte tipos de string a tipos llvmlite si es necesario
        if isinstance(return_type, str):
            return_type = self._llvm_type(return_type)
        
        param_types = [self._llvm_type(t) if isinstance(t, str) else t for t in param_types]
        
        # Crea el tipo de función
        func_type = ir.FunctionType(return_type, param_types)
        
        # Crea la función en el módulo
        func = ir.Function(self.module, func_type, name=name)
        
        # Registra en la tabla de funciones
        self.functions[name] = {
            "function": func,
            "return_type": return_type,
            "param_types": param_types
        }
        
        return func
    
    def _generate_print(self, expr_node):
        expr_value = self._generate_expression(expr_node)
        expr_type = self._get_expression_type(expr_node)

        try:
            printf = self.module.get_global("printf")
        except KeyError:
            printf_type = ir.FunctionType(self.int_type, [self.char_ptr_type], var_arg=True)
            printf = ir.Function(self.module, printf_type, name="printf")

        # Seleccionar el formato adecuado
        if isinstance(expr_type, ir.IntType) and expr_type.width == 32:
            fmt_str = "%d\n\0"
        elif isinstance(expr_type, ir.DoubleType):
            fmt_str = "%f\n\0"
        else:
            fmt_str = "%s\n\0"

        # Si ya existe esta cadena de formato, reutilizarla
        if fmt_str not in self.string_constants:
            byte_array = bytearray(fmt_str.encode("utf8"))
            fmt = ir.Constant(ir.ArrayType(ir.IntType(8), len(byte_array)), byte_array)
            global_fmt = ir.GlobalVariable(self.module, fmt.type, name=f"fmt.{len(self.string_constants)}")
            global_fmt.linkage = "internal"
            global_fmt.global_constant = True
            global_fmt.initializer = fmt
            self.string_constants[fmt_str] = global_fmt
        else:
            global_fmt = self.string_constants[fmt_str]

        fmt_ptr = self.builder.bitcast(global_fmt, self.char_ptr_type)
        self.builder.call(printf, [fmt_ptr, expr_value])

    def _generate_if_statement(self, node):
        """Genera estructura if-else"""
        conditions = node.children[0].children
        blocks = node.children[1].children
        else_block = node.children[2] if len(node.children) > 2 else None
        
        # Crear bloques básicos
        end_block = self.builder.append_basic_block("if.end")
        
        for i, (cond, block) in enumerate(zip(conditions, blocks)):
            # Generar condición
            cond_value = self._generate_expression(cond)
            
            # Crear bloques para then y else
            then_block = self.builder.append_basic_block(f"if.then{i}")
            next_block = self.builder.append_basic_block(f"if.else{i}") if i < len(conditions)-1 or else_block else end_block
            
            # Saltar según condición
            self.builder.cbranch(cond_value, then_block, next_block)
            
            # Generar bloque then
            self.builder.position_at_end(then_block)
            self._generate_node(block)
            self.builder.branch(end_block)
            
            # Posicionarse para siguiente condición
            self.builder.position_at_end(next_block)
        
        # Generar bloque else si existe
        if else_block:
            self._generate_node(else_block)
            if not self.builder.block.is_terminated:
                self.builder.branch(end_block)
        
    # Ensure we're positioned at the end block
        self.builder.position_at_end(end_block)
        if not end_block.is_terminated:
            # Add a default terminator if needed
            if (self.current_function and 
                self.current_function.function_type.return_type != self.void_type):
                self.builder.ret(Constant(self.current_function.function_type.return_type, 0))


    def _generate_while_loop(self, node):
        """Genera estructura while"""
        cond = node.children[0]
        body = node.children[1]
        
        # Crear bloques básicos
        cond_block = self.builder.append_basic_block("while.cond")
        body_block = self.builder.append_basic_block("while.body")
        end_block = self.builder.append_basic_block("while.end")
        
        # Saltar a condición
        self.builder.branch(cond_block)
        
        # Generar condición
        self.builder.position_at_end(cond_block)
        cond_value = self._generate_expression(cond)
        self.builder.cbranch(cond_value, body_block, end_block)
        
        # Generar cuerpo
        self.builder.position_at_end(body_block)
        self._generate_node(body)
        self.builder.branch(cond_block)  # Volver a condición
        
        # Continuar después del while
        self.builder.position_at_end(end_block)

    def _generate_for_loop(self, node):
        """Genera estructura for"""
        init, cond, update, body = node.children
        
        # Crear bloques básicos
        cond_block = self.builder.append_basic_block("for.cond")
        body_block = self.builder.append_basic_block("for.body")
        update_block = self.builder.append_basic_block("for.update")
        end_block = self.builder.append_basic_block("for.end")
        
        # Generar inicialización
        self._generate_node(init)
        self.builder.branch(cond_block)
        
        # Generar condición
        self.builder.position_at_end(cond_block)
        cond_value = self._generate_expression(cond)
        self.builder.cbranch(cond_value, body_block, end_block)
        
        # Generar cuerpo
        self.builder.position_at_end(body_block)
        self._generate_node(body)
        self.builder.branch(update_block)
        
        # Generar actualización
        self.builder.position_at_end(update_block)
        self._generate_node(update)
        self.builder.branch(cond_block)  # Volver a condición
        
        # Continuar después del for
        self.builder.position_at_end(end_block)

    def _generate_function_decl(self, node):
        """Genera declaración de función"""
        func_name = node.value
        return_type = self._llvm_type(node.children[0].value)
        params = node.children[1].children
        body_node = node.children[2]
        
        # Crear tipos de parámetros
        param_types = [self._llvm_type(p.children[0].value) for p in params]
        func_type = ir.FunctionType(return_type, param_types)
        
        # Crear función
        func = ir.Function(self.module, func_type, name=func_name)
        
        # Guardar contexto actual
        old_function = self.current_function
        old_symbol_table = self.symbol_table.copy()
        old_builder = self.builder
        
        # Establecer nuevo contexto
        self.current_function = func  # <- ESTA LÍNEA ES IMPORTANTE
        self.symbol_table = {}
        entry_block = func.append_basic_block("entry")
        self.builder = IRBuilder(entry_block)
        
        # Almacenar parámetros
        for i, (param, param_node) in enumerate(zip(func.args, params)):
            param_name = param_node.value
            ptr = self.builder.alloca(param.type, name=f"{param_name}.addr")
            self.builder.store(param, ptr)
            self.symbol_table[param_name] = ptr
        
        # Generar cuerpo
        self._generate_node(body_node)
        
        # Asegurar retorno si es necesario
        if not entry_block.is_terminated: 
            if return_type == self.int_type:
                self.builder.ret(Constant(self.int_type, 0))
            elif return_type == self.double_type:
                self.builder.ret(Constant(self.double_type, 0.0))
            elif return_type == self.bool_type:
                self.builder.ret(Constant(self.bool_type, 0))            
            elif return_type != self.void_type:
                self.builder.ret_void()
            else:
                raise Exception(f"Unhandled return type in function '{func_name}'")
        
        # Restaurar contexto
        self.current_function = old_function
        self.symbol_table = old_symbol_table
        self.builder = old_builder
        
        # Registrar función
        self.functions[func_name] = {
            "function": func,
            "return_type": return_type,
            "param_types": param_types
        }

    def _generate_function_call(self, node):
        """Genera llamada a función"""
        func_name = node.value
        args = [self._generate_expression(arg) for arg in node.children]
        
        if func_name in self.functions:
            func = self.functions[func_name]["function"]
            return self.builder.call(func, args)
        else:
            # Verificar si la función ya existe en el módulo
            func = self.module.get_global(func_name)
            if func is None:
                # Asumir función externa (como printf)
                func_type = ir.FunctionType(self.int_type, [self.char_ptr_type], var_arg=True)
                func = ir.Function(self.module, func_type, name=func_name)
            return self.builder.call(func, args)

    def _generate_return(self, node):
        if self.builder.block.is_terminated:
            return  # Ya está terminado, no hacer nada

        if len(node.children) > 0:
            ret_value = self._generate_expression(node.children[0])
        else:
            ret_value = None
        
        self.builder.ret(ret_value)


    def _generate_expression(self, node):
        """Genera código para expresiones"""
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
            return Constant(self.int_type, 0)  # Valor por defecto

    def _generate_literal(self, node):
        """Genera constantes literales"""
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
        """Genera constantes de cadena"""
        # Crear constante global para la cadena
        str_type = ir.ArrayType(ir.IntType(8), len(value) + 1)
        str_const = ir.Constant(str_type, bytearray(value.encode('utf-8') + b'\x00'))
        
        # Crear variable global
        global_str = ir.GlobalVariable(self.module, str_type, name=f"str.{len(self.string_constants)}")
        global_str.linkage = "internal"
        global_str.global_constant = True
        global_str.initializer = str_const
        self.string_constants[value] = global_str
        
        # Obtener puntero al primer carácter
        zero = Constant(ir.IntType(32), 0)
        return self.builder.gep(global_str, [zero, zero], name="strptr")

    def _generate_variable(self, node):
        """Genera acceso a variable"""
        var_name = node.value
        ptr = self.symbol_table[var_name]
        return self.builder.load(ptr, name=f"{var_name}.val")

    def _generate_binary_op(self, node):
        """Genera operaciones binarias"""
        left = self._generate_expression(node.children[0])
        right = self._generate_expression(node.children[1])
        op = node.value
        
        # Determinar tipo resultante
        left_type = self._get_expression_type(node.children[0])
        right_type = self._get_expression_type(node.children[1])
        
        # Convertir tipos si es necesario
        if left_type != right_type:
            if isinstance(left_type, ir.IntType) and isinstance(right_type, ir.DoubleType):
                left = self.builder.sitofp(left, right_type)
            elif isinstance(left_type, ir.DoubleType) and isinstance(right_type, ir.IntType):
                right = self.builder.sitofp(right, left_type)
        
        # Realizar operación
        if op in ["+", "-", "*", "/"]:
            if isinstance(left_type, ir.DoubleType):
                if op == "+": return self.builder.fadd(left, right)
                elif op == "-": return self.builder.fsub(left, right)
                elif op == "*": return self.builder.fmul(left, right)
                else: return self.builder.fdiv(left, right)
            else:
                if op == "+": return self.builder.add(left, right)
                elif op == "-": return self.builder.sub(left, right)
                elif op == "*": return self.builder.mul(left, right)
                else: return self.builder.sdiv(left, right)
        elif op in ["<", ">", "<=", ">=", "==", "!="]:
            if isinstance(left_type, ir.DoubleType):
                if op == "<": return self.builder.fcmp_ordered("<", left, right)
                elif op == ">": return self.builder.fcmp_ordered(">", left, right)
                elif op == "<=": return self.builder.fcmp_ordered("<=", left, right)
                elif op == ">=": return self.builder.fcmp_ordered(">=", left, right)
                elif op == "==": return self.builder.fcmp_ordered("==", left, right)
                else: return self.builder.fcmp_ordered("!=", left, right)
            else:
                if op == "<": return self.builder.icmp_signed("<", left, right)
                elif op == ">": return self.builder.icmp_signed(">", left, right)
                elif op == "<=": return self.builder.icmp_signed("<=", left, right)
                elif op == ">=": return self.builder.icmp_signed(">=", left, right)
                elif op == "==": return self.builder.icmp_signed("==", left, right)
                else: return self.builder.icmp_signed("!=", left, right)

    def _generate_unary_op(self, node):
        """Genera operaciones unarias"""
        operand = self._generate_expression(node.children[0])
        op = node.value
        
        if op == "-":
            if isinstance(operand.type, ir.DoubleType):
                return self.builder.fneg(operand)
            else:
                return self.builder.sub(Constant(operand.type, 0), operand)
        elif op in ["++", "--"]:
            # Manejar incremento/decremento
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
            return new_value  # Retorna el nuevo valor

    def _llvm_type(self, type_str):
        """Convierte tipo de string a tipo llvmlite"""
        type_map = {
            "entero": self.int_type,
            "decimal": self.double_type,
            "cadena": self.char_ptr_type,
            "bool": self.bool_type,
            "void": self.void_type
        }
        return type_map.get(type_str, self.int_type)

    def _get_expression_type(self, node):
        """Obtiene el tipo llvmlite de una expresión"""
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
            ptr = self.symbol_table[node.value]
            return ptr.type.pointee
        elif node.type == "BinaryOp":
            left_type = self._get_expression_type(node.children[0])
            right_type = self._get_expression_type(node.children[1])
            
            # Para operaciones aritméticas, devolver el tipo más amplio
            if node.value in ["+", "-", "*", "/"]:
                if isinstance(left_type, ir.DoubleType) or isinstance(right_type, ir.DoubleType):
                    return self.double_type
                return self.int_type
            # Para comparaciones, devolver booleano
            else:
                return self.bool_type
        elif node.type == "UnaryOp":
            return self._get_expression_type(node.children[0])
        elif node.type == "FunctionCall":
            if node.value in self.functions:
                return self.functions[node.value]["return_type"]
            return self.int_type  # Por defecto
        
        return self.int_type  # Tipo por defecto

    def save_to_file(self, filename="output.ll"):
        """Guarda el módulo LLVM en un archivo"""
        llvm_ir = str(self.module)
        print("\nGenerated IR:\n" + "="*50)
        print(llvm_ir)
        print("="*50 + "\n")
        
        with open(filename, 'w') as f:
            f.write(llvm_ir)
        print(f"LLVM IR guardado en {filename}")

    def compile_to_llvm(self, ast):
        """Método principal para compilar AST a LLVM"""
        self.generate_code(ast)
        return str(self.module)