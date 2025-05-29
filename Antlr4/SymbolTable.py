class SymbolTable:
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

    def define_function(self, name, params, return_type):
        """Define una función con sus parámetros y tipo de retorno"""
        self.funciones[name] = {
            'params': params,
            'return_type': return_type,
            'scope_level': len(self.ambitos)  # Guardar nivel de scope
        }
        
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
    
    def get_variable_in_current_scope(self, name):
        """Busca la variable solo en el ámbito actual (más interno)."""
        if not self.ambitos:
            return None
        return self.ambitos[-1].get(name, None)
    
    def get_variable_type(self, name):
        """Devuelve el tipo de una variable si existe, de lo contrario, retorna None."""
        value = self.get_variable(name)
        print(value)
        return value
        
    def get_function_params(self, nombre_funcion):
        """Obtiene los parámetros de una función, si existen en el ámbito local."""
        if nombre_funcion in self.funciones:
            return self.funciones[nombre_funcion]
        return None
    
    def get_function_return_type(self, name):
        """Obtiene el tipo de retorno de una función"""
        if name in self.funciones:
            return self.funciones[name]['return_type']
        return None
    
    def get_function(self, name):
        """Obtiene la información completa de una función (parámetros y tipo de retorno)."""
        if name in self.funciones:
            return self.funciones[name]
        return None