from antlr4 import *

class ExprBaseVisitor(ParseTreeVisitor):
    def __init__(self):
        self.variables = {} #variables globales
        self.ambitos = [{}]  # Stack de ámbitos (inicia con ámbito global)
        self.funciones = {}  # Diccionario de funciones

    def enter_scope(self):
        """Crear un nuevo ámbito (nuevo diccionario en la pila)."""
        self.ambitos.append({})

    def exit_scope(self):
        """Eliminar el último ámbito (salir del bloque actual)."""
        self.ambitos.pop()

    def define_variable(self, name, value):
        """Define una variable en el ámbito actual."""
        self.ambitos[-1][name] = value

    def get_variable(self, name):
        """Busca la variable en los ámbitos disponibles (de local a global)."""
        for scope in reversed(self.ambitos):
            if name in scope:
                return scope[name]
        raise NameError(f"Variable no definida: {name}")

    def visitDeclaracion(self, ctx):
        """Maneja la declaración de variables."""
        var_name = ctx.VARIABLE().getText()
        value = self.visit(ctx.expr())  # Obtener el valor de la expresión
        self.define_variable(var_name, value)

    def visitReasignacion(self, ctx):
        """Maneja la reasignación de variables."""
        var_name = ctx.VARIABLE().getText()
        value = self.visit(ctx.expr())
        
        # Buscar en los ámbitos y reasignar
        for scope in reversed(self.ambitos):
            if var_name in scope:
                scope[var_name] = value
                return
        raise NameError(f"Variable no definida: {var_name}")

    def traducir_tipo( tipo):
        if isinstance(tipo, int):
            return "entero"
        elif isinstance(tipo, float):
            return "decimal"
        elif isinstance(tipo, str):
            return "cadena"
        elif isinstance(tipo, float):
            return "bool"
        else:
            raise ValueError(f"El tipo de dato no es el correcto: {tipo}")
