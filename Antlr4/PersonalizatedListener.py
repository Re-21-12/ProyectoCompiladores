from antlr4 import *

if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

class PersonalizatedListener(ParseTreeListener):
    
    def __init__(self):
        # Tabla de símbolos con stack para manejo de ámbitos
        self.symbol_table_stack = [{}]  # Stack de ámbitos (global primero)
        self.functions = {}  # Diccionario de funciones
        self.current_function = None
        self.errors = []
        self.warnings = []
    
    # ==============================================
    # HELPERS PARA MANEJO DE ÁMBITOS Y TABLA DE SÍMBOLOS
    # ==============================================
    
    def enter_scope(self):
        """Crea un nuevo ámbito (nuevo diccionario en la pila)"""
        self.symbol_table_stack.append({})
    
    def exit_scope(self):
        """Elimina el último ámbito (sale del bloque actual)"""
        if len(self.symbol_table_stack) > 1:  # No quitamos el ámbito global
            self.symbol_table_stack.pop()
    
    def add_symbol(self, name, type_info, ctx=None):
        """Añade un símbolo al ámbito actual"""
        if name in self.symbol_table_stack[-1]:
            self.add_error(f"Variable '{name}' ya declarada en este ámbito", ctx)
            return False
        self.symbol_table_stack[-1][name] = {
            'type': type_info,
            'initialized': False
        }
        return True
    
    def get_symbol(self, name, ctx=None):
        """Busca un símbolo en los ámbitos disponibles (de local a global)"""
        for scope in reversed(self.symbol_table_stack):
            if name in scope:
                return scope[name]
        self.add_error(f"Variable '{name}' no declarada", ctx)
        return None
    
    def add_error(self, message, ctx=None):
        """Registra un error con información de posición"""
        if ctx:
            line = ctx.start.line
            column = ctx.start.column
            self.errors.append(f"Línea {line}:{column} - {message}")
        else:
            self.errors.append(message)
    
    def add_warning(self, message, ctx=None):
        """Registra una advertencia con información de posición"""
        if ctx:
            line = ctx.start.line
            column = ctx.start.column
            self.warnings.append(f"Línea {line}:{column} - {message}")
        else:
            self.warnings.append(message)
    
    # ==============================================
    # MANEJO DE FUNCIONES
    # ==============================================
    
    def enterDeclaracion_funcion(self, ctx: ExprParser.Declaracion_funcionContext):
        nombre_funcion = ctx.VARIABLE().getText()
        if nombre_funcion in self.functions:
            self.add_error(f"Función '{nombre_funcion}' ya declarada", ctx)
            return
        
        # Obtener parámetros
        parametros = []
        if ctx.parametros():
            for param in ctx.parametros().parametro():
                param_name = param.VARIABLE().getText()
                param_type = param.tipo().getText()
                parametros.append((param_name, param_type))
        
        # Registrar función
        self.functions[nombre_funcion] = {
            'params': parametros,
            'return_type': ctx.tipo().getText() if ctx.tipo() else None
        }
        self.current_function = nombre_funcion
        self.enter_scope()  # Nuevo ámbito para la función
        
        # Registrar parámetros como variables
        for param_name, param_type in parametros:
            self.add_symbol(param_name, param_type, ctx)
    
    def exitDeclaracion_funcion(self, ctx:ExprParser.Declaracion_funcionContext):
        self.exit_scope()
        self.current_function = None
    
    def enterFuncion_llamada(self, ctx: ExprParser.Funcion_llamadaContext):
        nombre_funcion = ctx.VARIABLE().getText()
        if nombre_funcion not in self.functions:
            self.add_error(f"Función '{nombre_funcion}' no declarada", ctx)
            return
        
        # Verificar número de argumentos
        expected_args = len(self.functions[nombre_funcion]['params'])
        actual_args = len(ctx.argumentos().expr()) if ctx.argumentos() else 0
        
        if expected_args != actual_args:
            self.add_error(
                f"Función '{nombre_funcion}' espera {expected_args} argumentos pero recibió {actual_args}", 
                ctx
            )
    
    # ==============================================
    # MANEJO DE VARIABLES Y DECLARACIONES
    # ==============================================
    
    def enterDeclaracion(self, ctx: ExprParser.DeclaracionContext):
        var_name = ctx.VARIABLE().getText()
        var_type = ctx.tipo().getText()
        
        # Registrar variable
        if not self.add_symbol(var_name, var_type, ctx):
            return
        
        # Si hay expresión, verificar compatibilidad de tipos
        if ctx.expr():
            expr_type = self.infer_expr_type(ctx.expr())
            if expr_type and expr_type != var_type:
                self.add_error(
                    f"Tipo incompatible: no se puede asignar '{expr_type}' a variable de tipo '{var_type}'", 
                    ctx
                )
    
    def enterReasignacion(self, ctx: ExprParser.ReasignacionContext):
        var_name = ctx.VARIABLE().getText()
        var_info = self.get_symbol(var_name, ctx)
        if not var_info:
            return
        
        # Verificar tipo de expresión
        expr_type = self.infer_expr_type(ctx.expr())
        if expr_type and expr_type != var_info['type']:
            self.add_error(
                f"Tipo incompatible: no se puede asignar '{expr_type}' a variable de tipo '{var_info['type']}'", 
                ctx
            )
    
    # ==============================================
    # ESTRUCTURAS DE CONTROL
    # ==============================================
    
    def enterSentencia_if(self, ctx:ExprParser.Sentencia_ifContext):
        # Verificar que la condición sea booleana
        cond_type = self.infer_expr_type(ctx.bloque_condicional().expr())
        if cond_type and cond_type != 'bool':
            self.add_error(
                f"La condición del if debe ser booleana, no '{cond_type}'", 
                ctx.bloque_condicional()
            )
        
        # Entrar en ámbito para el bloque if
        self.enter_scope()
    
    def exitSentencia_if(self, ctx:ExprParser.Sentencia_ifContext):
        # Salir del ámbito del if
        self.exit_scope()
        
        # Manejar ámbitos de elif y else si existen
        for i in range(1, len(ctx.bloque_condicional())):
            self.exit_scope()  # Salir del ámbito de cada elif
        
        if ctx.ELSE():
            self.exit_scope()  # Salir del ámbito del else
    
    def enterBloque_condicional(self, ctx:ExprParser.Bloque_condicionalContext):
        # Entrar en nuevo ámbito para cada bloque condicional (if/elif/else)
        self.enter_scope()
    
    def enterSentencia_while(self, ctx:ExprParser.Sentencia_whileContext):
        # Verificar que la condición sea booleana
        cond_type = self.infer_expr_type(ctx.bloque_condicional().expr())
        if cond_type and cond_type != 'bool':
            self.add_error(
                f"La condición del while debe ser booleana, no '{cond_type}'", 
                ctx.bloque_condicional()
            )
        
        self.enter_scope()  # Nuevo ámbito para el bloque while
    
    def exitSentencia_while(self, ctx:ExprParser.Sentencia_whileContext):
        self.exit_scope()  # Salir del ámbito del while
    
    def enterSentencia_for(self, ctx:ExprParser.Sentencia_forContext):
        self.enter_scope()  # Nuevo ámbito para el for
    
    def exitSentencia_for(self, ctx:ExprParser.Sentencia_forContext):
        self.exit_scope()  # Salir del ámbito del for
    
    # ==============================================
    # INFERENCIA DE TIPOS
    # ==============================================
    
    def infer_expr_type(self, ctx):
        """Infiere el tipo de una expresión recursivamente"""
        if ctx.NUMERO():
            return 'entero'
        elif ctx.DECIMAL():
            return 'decimal'
        elif ctx.CADENA():
            return 'cadena'
        elif ctx.BOOLEANO():
            return 'bool'
        elif ctx.VARIABLE():
            var_info = self.get_symbol(ctx.VARIABLE().getText())
            return var_info['type'] if var_info else None
        elif ctx.funcion_llamada():
            func_name = ctx.funcion_llamada().VARIABLE().getText()
            return self.functions.get(func_name, {}).get('return_type')
        elif ctx.expr():
            # Manejar operaciones binarias
            if ctx.getChildCount() == 3:  # Operación binaria
                left_type = self.infer_expr_type(ctx.expr(0))
                right_type = self.infer_expr_type(ctx.expr(1))
                op = ctx.getChild(1).getText()
                
                # Verificar compatibilidad de tipos
                if left_type != right_type:
                    self.add_error(
                        f"Tipos incompatibles en operación: '{left_type}' {op} '{right_type}'", 
                        ctx
                    )
                    return None
                
                # Determinar tipo resultante
                if op in ['+', '-', '*', '/']:
                    if left_type in ['entero', 'decimal']:
                        return 'decimal' if 'decimal' in [left_type, right_type] else 'entero'
                elif op in ['<', '>', '<=', '>=', '==', '!=']:
                    return 'bool'
                
            return self.infer_expr_type(ctx.expr(0))
        
        return None
    
    # ==============================================
    # MÉTODOS RESTANTES (pueden dejarse vacíos)
    # ==============================================
    
    def enterGramatica(self, ctx:ExprParser.GramaticaContext): pass
    def exitGramatica(self, ctx:ExprParser.GramaticaContext): pass
    def enterPrograma(self, ctx:ExprParser.ProgramaContext): pass
    def exitPrograma(self, ctx:ExprParser.ProgramaContext): pass
    def enterBloque(self, ctx:ExprParser.BloqueContext): 
        self.enter_scope()
    def exitBloque(self, ctx:ExprParser.BloqueContext): 
        self.exit_scope()
    def enterSentencia(self, ctx:ExprParser.SentenciaContext): pass
    def exitSentencia(self, ctx:ExprParser.SentenciaContext): pass
    def enterMostrar(self, ctx:ExprParser.MostrarContext): pass
    def exitMostrar(self, ctx:ExprParser.MostrarContext): pass
    def exitDeclaracion(self, ctx:ExprParser.DeclaracionContext): pass
    def exitReasignacion(self, ctx:ExprParser.ReasignacionContext): pass
    def exitFuncion_llamada(self, ctx:ExprParser.Funcion_llamadaContext): pass