from llvmlite import ir, binding
class LLVMGenerator:
    def __init__(self):
        self.module = ir.Module(name="module")
        self.builder = None
        self.funcs = {}
        self.variables = {}
        
    def generate(self, ast):
        return self.visit(ast)
    
    def visit(self, node):
        method_name = f'visit_{node.type}'
        method = getattr(self, method_name, self.generic_visit)
        return method(node)
    
    def generic_visit(self, node):
        raise Exception(f'No visit_{node.type} method')
    
    def visit_Gramatica(self, node):
        for child in node.children:
            self.visit(child)
            
    def visit_Programa(self, node):
        for child in node.children:
            self.visit(child)
        return self.module
    
    def visit_DeclaracionFuncion(self, node):
        # Suponemos que la función retorna un valor entero
        func_type = ir.FunctionType(ir.IntType(32), [ir.IntType(32)] * len(node.children[:-2]))  # Ajustar tipos según los parámetros
        func = ir.Function(self.module, func_type, name=node.value)
        block = func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)
        self.funcs[node.value] = func
        
        # Asignar los parámetros
        for i, arg in enumerate(func.args):
            arg.name = f'arg{i}'
            self.variables[arg.name] = arg
        
        self.visit(node.children[-2])  # Llamar al bloque de la función
        if node.children[-1]:  # Si hay un valor de retorno
            return_val = self.visit(node.children[-1])
            self.builder.ret(return_val)
        else:
            self.builder.ret(ir.Constant(ir.IntType(32), 0))  # Retorno por defecto (0)
        return func
    
    def visit_Bloque(self, node):
        for child in node.children:
            self.visit(child)
    
    def visit_Sentencia(self, node):
        for child in node.children:
            self.visit(child)
    
    def visit_Sentencia_if(self, node):
        cond_block = self.builder.function.append_basic_block(name="if_cond")
        body_block = self.builder.function.append_basic_block(name="if_body")
        after_block = self.builder.function.append_basic_block(name="if_after")
        
        self.builder.branch(cond_block)
        self.builder.position_at_end(cond_block)
        condition = self.visit(node.children[0])
        self.builder.cbranch(condition, body_block, after_block)
        
        self.builder.position_at_end(body_block)
        self.visit(node.children[1])
        if len(node.children) > 2 and node.children[2]:
            self.builder.branch(after_block)
        
        self.builder.position_at_end(after_block)
    
    def visit_Sentencia_while(self, node):
        func = self.builder.function
        cond_block = func.append_basic_block(name="while_cond")
        body_block = func.append_basic_block(name="while_body")
        after_block = func.append_basic_block(name="while_after")
        
        self.builder.branch(cond_block)
        self.builder.position_at_end(cond_block)
        condition = self.visit(node.children[0])
        self.builder.cbranch(condition, body_block, after_block)
        
        self.builder.position_at_end(body_block)
        self.visit(node.children[1])
        self.builder.branch(cond_block)
        
        self.builder.position_at_end(after_block)
    
    def visit_Sentencia_for(self, node):
        func = self.builder.function
        if node.children[0]:
            self.visit(node.children[0])  # Inicialización
        
        cond_block = func.append_basic_block(name="for_cond")
        body_block = func.append_basic_block(name="for_body")
        update_block = func.append_basic_block(name="for_update")
        after_block = func.append_basic_block(name="for_after")
        
        self.builder.branch(cond_block)
        self.builder.position_at_end(cond_block)
        condition = self.visit(node.children[1])  # Condición del for
        self.builder.cbranch(condition, body_block, after_block)
        
        self.builder.position_at_end(body_block)
        self.visit(node.children[3])  # Bloque del cuerpo del for
        self.builder.branch(update_block)
        
        self.builder.position_at_end(update_block)
        self.visit(node.children[2])  # Actualización
        self.builder.branch(cond_block)
        
        self.builder.position_at_end(after_block)
    
    def visit_Reasignacion(self, node):
        value = self.visit(node.children[0])
        ptr = self.variables[node.value]
        self.builder.store(value, ptr)
    
    def visit_Expr(self, node):
        left = self.visit(node.children[0])
        right = self.visit(node.children[1])
        op = node.value
        if op == '+':
            return self.builder.add(left, right)
        elif op == '-':
            return self.builder.sub(left, right)
        elif op == '*':
            return self.builder.mul(left, right)
        elif op == '/':
            return self.builder.sdiv(left, right)
    
    def visit_Mostrar(self, node):
        value = self.visit(node.children[0])
        return value
    
    def visit_Declaracion(self, node):
        tipo = self.visit(node.children[0])
        nombre = node.value
        valor = self.visit(node.children[1]) if node.children else None
        var_type = ir.IntType(32)  # Asumimos tipo entero
        var_ptr = self.builder.alloca(var_type, name=nombre)  # Declaración de variable
        self.builder.store(valor, var_ptr)
        self.variables[nombre] = var_ptr
    
    def visit_Funcion_llamada(self, node):
        func = self.funcs[node.value]
        args = [self.visit(arg) for arg in node.children]
        return self.builder.call(func, args)
    
    def save_to_file(self, filename="output.ll"):
        with open(filename, "w") as f:
            f.write(str(self.module))
