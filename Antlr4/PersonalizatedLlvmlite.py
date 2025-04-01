from llvmlite import ir
import platform

class LLVMGenerator:
    def __init__(self):
        self.module = ir.Module(name="module")
        self._set_target_platform()
        
        self.builder = None
        self.funcs = {}
        self.variables = {}
        self.global_vars = {}
        self.current_function = None
        self.string_constants = {}
        self.string_counter = 0


    def _set_target_platform(self):
        """Configura la plataforma objetivo según el sistema operativo"""
        system = platform.system().lower()
        machine = platform.machine().lower()
        
        if system == "linux":
            self.module.triple = f"{machine}-pc-linux-gnu"
            self.module.data_layout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
        elif system == "darwin":  # macOS
            self.module.triple = f"{machine}-apple-darwin"
            self.module.data_layout = "e-m:o-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
        elif system == "windows":
            self.module.triple = f"{machine}-pc-windows-msvc"
            self.module.data_layout = "e-m:w-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
        else:
            self.module.triple = "x86_64-unknown-linux-gnu"  # Valor por defecto
            self.module.data_layout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
        

    def generate(self, ast):
        """Genera el código LLVM a partir del AST"""
        try:
            # Procesar declaraciones globales primero
            self.process_global_declarations(ast)
            
            # Crear función main si no hay funciones definidas
            if not self.funcs:
                self.create_main_function(ast)
                
            return self.module
        except Exception as e:
            print(e)
            raise

    def save_to_file(self, filename="output.ll"):
        """Guarda el módulo LLVM en un archivo"""
        with open(filename, "w") as f:
            f.write(str(self.module))
        return filename

    def process_global_declarations(self, ast):
        if ast and ast.type == "Programa":
            for child in ast.children:
                if child and child.type == "Declaracion":
                    self.visit_Declaracion(child)

    def create_main_function(self, ast):
        # Crear función main
        func_type = ir.FunctionType(ir.IntType(32), [])
        func = ir.Function(self.module, func_type, name="main")
        block = func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)
        self.funcs["main"] = func
        self.current_function = func
        
        # Procesar el contenido del programa
        if ast and ast.type == "Programa":
            for child in ast.children:
                if child and child.type not in ["DeclaracionFuncion", "Declaracion"]:
                    self.visit(child)
        
        # Finalizar la función main
        if self.builder.block.terminator is None:
            self.builder.ret(ir.Constant(ir.IntType(32), 0))

    def visit(self, node):
        if node is None:
            return None
            
        method_name = f'visit_{node.type}'
        method = getattr(self, method_name, self.generic_visit)
        return method(node)
        
    def generic_visit(self, node):
        for child in node.children:
            self.visit(child)
        return None

    def visit_Programa(self, node):
        for child in node.children:
            self.visit(child)
        return self.module

    def visit_DeclaracionFuncion(self, node):
        return_type = self.get_llvm_type(node.children[0].value)
        param_types = [self.get_llvm_type(child.children[0].value) for child in node.children[1:-2] if child.type == "Parametro"]
        
        func_type = ir.FunctionType(return_type, param_types)
        func = ir.Function(self.module, func_type, name=node.value)
        block = func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)
        self.funcs[node.value] = func
        self.current_function = func
        
        for i, arg in enumerate(func.args):
            arg.name = node.children[1+i].value
            alloca = self.builder.alloca(arg.type, name=arg.name)
            self.builder.store(arg, alloca)
            self.variables[arg.name] = alloca
        
        self.visit(node.children[-2])  # Bloque de código
        
        if not self.builder.block.terminator:
            if return_type == ir.VoidType():
                self.builder.ret_void()
            else:
                self.builder.ret(ir.Constant(return_type, 0))
        
        return func

    def visit_Declaracion(self, node):
        var_type = self.get_llvm_type(node.children[0].value)
        name = node.value
        
        if self.current_function:  # Variable local
            alloca = self.builder.alloca(var_type, name=name)
            self.variables[name] = alloca
            if len(node.children) > 1:
                value = self.visit(node.children[1])
                self.builder.store(value, alloca)
        else:  # Variable global
            gvar = ir.GlobalVariable(self.module, var_type, name=name)
            gvar.linkage = 'internal'
            if len(node.children) > 1:
                init_val = self.get_constant_value(node.children[1])
                gvar.initializer = init_val
            else:
                gvar.initializer = ir.Constant(var_type, 0)
            self.global_vars[name] = gvar

    def visit_Expr(self, node):
        if len(node.children) == 1:
            return self.visit(node.children[0])
        
        left = self.visit(node.children[0])
        right = self.visit(node.children[1])
        
        if node.value == '+':
            return self.builder.add(left, right, name="addtmp")
        elif node.value == '-':
            return self.builder.sub(left, right, name="subtmp")
        elif node.value == '*':
            return self.builder.mul(left, right, name="multmp")
        elif node.value == '/':
            return self.builder.sdiv(left, right, name="divtmp")

    def visit_Reasignacion(self, node):
        value = self.visit(node.children[0])
        ptr = self.variables.get(node.value) or self.global_vars.get(node.value)
        self.builder.store(value, ptr)

    def visit_Sentencia_if(self, node):
        cond = self.visit(node.children[0])
        
        func = self.builder.function
        then_block = func.append_basic_block(name="then")
        else_block = func.append_basic_block(name="else") if len(node.children) > 2 else None
        merge_block = func.append_basic_block(name="ifcont")
        
        self.builder.cbranch(cond, then_block, else_block if else_block else merge_block)
        
        self.builder.position_at_end(then_block)
        self.visit(node.children[1])
        if not self.builder.block.terminator:
            self.builder.branch(merge_block)
        
        if else_block:
            self.builder.position_at_end(else_block)
            self.visit(node.children[2])
            if not self.builder.block.terminator:
                self.builder.branch(merge_block)
        
        self.builder.position_at_end(merge_block)

    def visit_Actualizacion(self, node):
        var_name = node.children[0].value
        ptr = self.variables.get(var_name) or self.global_vars.get(var_name)
        current_val = self.builder.load(ptr, name=f"{var_name}_val")
        
        if node.value == "++":
            new_val = self.builder.add(current_val, ir.Constant(ir.IntType(32), 1), name=f"{var_name}_inc")
        elif node.value == "--":
            new_val = self.builder.sub(current_val, ir.Constant(ir.IntType(32), 1), name=f"{var_name}_dec")
            
        self.builder.store(new_val, ptr)
        return new_val

    def visit_Mostrar(self, node):
        value = self.visit(node.children[0])
        
        # Configurar printf
        voidptr_ty = ir.IntType(8).as_pointer()
        printf_ty = ir.FunctionType(ir.IntType(32), [voidptr_ty], var_arg=True)
        printf = ir.Function(self.module, printf_ty, name="printf")
        
        # Determinar el formato según el tipo
        if isinstance(value.type, ir.IntType):
            fmt = "%d\n\0" if value.type.width == 32 else "%d\n\0"
        elif isinstance(value.type, ir.FloatType):
            fmt = "%f\n\0"
        else:
            fmt = "%d\n\0"
        
        # Crear constante de formato
        c_fmt = ir.Constant(ir.ArrayType(ir.IntType(8), len(fmt)), bytearray(fmt.encode("utf8")))
        global_fmt = ir.GlobalVariable(self.module, c_fmt.type, name="fstr")
        global_fmt.linkage = 'internal'
        global_fmt.global_constant = True
        global_fmt.initializer = c_fmt
        
        # Llamar a printf
        fmt_arg = self.builder.bitcast(global_fmt, voidptr_ty)
        self.builder.call(printf, [fmt_arg, value])
        return value

    def visit_Variable(self, node):
        ptr = self.variables.get(node.value) or self.global_vars.get(node.value)
        return self.builder.load(ptr, name=node.value)

    def visit_Literal(self, node):
        if isinstance(node.value, bool):
            return ir.Constant(ir.IntType(1), int(node.value))
        elif isinstance(node.value, int):
            return ir.Constant(ir.IntType(32), node.value)
        elif isinstance(node.value, float):
            return ir.Constant(ir.DoubleType(), node.value)
        elif isinstance(node.value, str):
            return self.create_string_constant(node.value)
        return ir.Constant(ir.IntType(32), 0)

    def create_string_constant(self, str_val):
        name = f".str.{self.string_counter}"
        self.string_counter += 1
        
        array_type = ir.ArrayType(ir.IntType(8), len(str_val)+1)
        constant = ir.Constant(array_type, bytearray((str_val + "\0").encode("utf8")))
        
        gvar = ir.GlobalVariable(self.module, array_type, name=name)
        gvar.linkage = 'internal'
        gvar.global_constant = True
        gvar.initializer = constant
        
        return self.builder.bitcast(gvar, ir.IntType(8).as_pointer())

    def get_llvm_type(self, type_str):
        type_map = {
            'entero': ir.IntType(32),
            'int': ir.IntType(32),
            'float': ir.FloatType(),
            'double': ir.DoubleType(),
            'bool': ir.IntType(1),
            'void': ir.VoidType(),
            'cadena': ir.IntType(8).as_pointer()
        }
        return type_map.get(type_str, ir.IntType(32))

    def get_constant_value(self, node):
        if node.type == "Literal":
            if isinstance(node.value, bool):
                return ir.Constant(ir.IntType(1), int(node.value))
            elif isinstance(node.value, int):
                return ir.Constant(ir.IntType(32), node.value)
            elif isinstance(node.value, float):
                return ir.Constant(ir.DoubleType(), node.value)
        return ir.Constant(ir.IntType(32), 0)