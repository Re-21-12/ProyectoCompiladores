from antlr4 import ParseTreeVisitor
class ExprBaseVisitor(ParseTreeVisitor):
    def __init__(self):
        self.ambitos = [{}]  # Stack de ámbitos (inicia con ámbito global)
        self.funciones = {}  # Diccionario de funciones (nombre: info)
        self.return_value = None
        self.should_return = False

    def enter_scope(self):
        """Crear un nuevo ámbito (nuevo diccionario en la pila)."""
        self.ambitos.append({})

    def exit_scope(self):
        """Eliminar el último ámbito (salir del bloque actual)."""
        if len(self.ambitos) > 1:  # No permitir eliminar el ámbito global
            self.ambitos.pop()

    def define_variable(self, name, value):
        """Define una variable en el ámbito actual."""
        self.ambitos[-1][name] = value

    def get_variable(self, name):
        """Busca la variable en los ámbitos disponibles (de local a global)."""
        for ambito in reversed(self.ambitos):
            if name in ambito:
                return ambito[name]
        raise Exception(f"Variable '{name}' no definida")

    def define_function(self, name, info):
        """Define una función en el ámbito global."""
        self.funciones[name] = info

    def get_function(self, name):
        """Obtiene la información de una función."""
        if name not in self.funciones:
            raise Exception(f"Función '{name}' no definida")
        return self.funciones[name]
    def get_function_return_type(self, name):
        """Obtiene el tipo de retorno de una función si está definida."""
        if name not in self.funciones:
            raise Exception(f"Función '{name}' no definida")
        return self.funciones[name]['return_type']
