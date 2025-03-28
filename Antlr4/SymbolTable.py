class SymbolTable:
    def __init__(self):
        self.symbols = {}
        self.scopes = [self.symbols]  # Usamos una lista para manejar los diferentes niveles de alcance

    def enter_scope(self):
        self.scopes.append({})  # Abrir un nuevo alcance (por ejemplo, dentro de una función)

    def exit_scope(self):
        self.scopes.pop()  # Salir del alcance actual

    def declare_variable(self, var_name, var_type):
        current_scope = self.scopes[-1]
        if var_name in current_scope:
            raise ValueError(f"Variable '{var_name}' ya declarada en este alcance.")
        current_scope[var_name] = var_type

    def get_variable(self, var_name):
        for scope in reversed(self.scopes):  # Buscamos la variable en el ámbito más cercano
            if var_name in scope:
                return scope[var_name]
        return None  # Variable no encontrada
