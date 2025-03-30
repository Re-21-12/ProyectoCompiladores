from antlr4 import ParseTreeVisitor

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

    def define_function(self, name, params):
        """Define una función y sus parámetros en el ámbito global."""
        self.funciones[name] = params  
        
    def define_function_params(self, nombre_funcion, args):
        """Define los parámetros de la función dentro de su ámbito local."""
        if nombre_funcion in self.funciones:
            self.enter_scope()  # Crear un ámbito para la función
            params = self.funciones[nombre_funcion]
            for param, arg in zip(params, args):
                self.define_variable(param, arg)        

    def get_variable(self, name):
        """Busca la variable en los ámbitos disponibles (de local a global)."""
        for ambito in reversed(self.ambitos):
            if name in ambito:
                return ambito[name]
        return None
    
    def get_variable_type(self, name):
        """Devuelve el tipo de una variable si existe, de lo contrario, retorna None."""
        value = self.get_variable(name)
        return type(value).__name__ if value is not None else None
    
    def get_function_params(self, nombre_funcion):
        """Obtiene los parámetros de una función, si existen en el ámbito local."""
        if nombre_funcion in self.funciones:
            return self.funciones[nombre_funcion]
        return None