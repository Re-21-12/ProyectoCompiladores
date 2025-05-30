class SymbolTable:
    def __init__(self):
        self.ambitos = [{}]  # Stack de ámbitos (inicia con ámbito global)
        self.funciones = {}  # Diccionario de funciones

    def enter_scope(self):
        self.ambitos.append({})
        print(f"DEBUG: Nuevo scope creado. Scopes actuales: {self.ambitos}")

    def exit_scope(self):
        if len(self.ambitos) > 1:
            self.ambitos.pop()
            print(f"DEBUG: Scope eliminado. Scopes actuales: {self.ambitos}")
        else:
            raise Exception("Error: No se puede salir del scope global.")

    def define_variable(self, name, value):
        if name in self.ambitos[-1]:
            raise Exception(f"Error: Variable '{name}' ya declarada en este scope.")
        self.ambitos[-1][name] = value

    def get_variable(self, name):
        """Busca una variable en todos los scopes, desde el más reciente hasta el global."""
        for ambito in reversed(self.ambitos):
            if name in ambito:
                return ambito[name]
        raise Exception(f"Error: Variable '{name}' no definida.")

    def get_variable_in_current_scope(self, name):
        """Busca una variable solo en el scope actual."""
        return self.ambitos[-1].get(name, None)

    def define_function(self, name, params, return_type):
        """Define una función con sus parámetros y tipo de retorno."""
        if name in self.funciones:
            raise Exception(f"Error: Función '{name}' ya definida.")
        self.funciones[name] = {
            'params': params,
            'return_type': return_type
        }
        print(f"DEBUG: Función '{name}' definida con parámetros {params} y tipo de retorno '{return_type}'.")

    def get_function(self, name):
        """Obtiene la información completa de una función."""
        if name in self.funciones:
            return self.funciones[name]
        raise Exception(f"Error: Función '{name}' no definida.")

    def get_function_return_type(self, name):
        """Obtiene el tipo de retorno de una función."""
        if name in self.funciones:
            return self.funciones[name]['return_type']
        raise Exception(f"Error: Función '{name}' no definida.")

    def get_variable_type(self, name):
        """Obtiene el tipo de una variable."""
        variable_info = self.get_variable(name)
        if variable_info is not None:
            return variable_info
        raise Exception(f"Error: Variable '{name}' no definida.")

    def get_current_scope(self):
        """Devuelve el scope actual (el último en la pila)."""
        return self.ambitos[-1]