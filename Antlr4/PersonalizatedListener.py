import SymbolTable
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser
from ExprListener import ExprListener
from SymbolTable import SymbolTable
from antlr4.error.ErrorListener import ErrorListener

class PersonalizatedListener(ExprListener, SymbolTable, ErrorListener):
    
    letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"
    digitos = "0123456789"
    
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.panic_mode = False  # Control para el modo pánico
        self.current_function = None  # Track current function

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"Error de sintaxis en la línea {line}, columna {column}: {msg}")

    # ----------------------- Grammar Rule Methods -----------------------

    def enterGramatica(self, ctx: ExprParser.GramaticaContext): pass
    def exitGramatica(self, ctx: ExprParser.GramaticaContext): pass
    def enterPrograma(self, ctx: ExprParser.ProgramaContext): pass
    def exitPrograma(self, ctx: ExprParser.ProgramaContext): pass
    def enterBloque(self, ctx: ExprParser.BloqueContext): pass
    def exitBloque(self, ctx: ExprParser.BloqueContext): pass
    def enterSentencia(self, ctx: ExprParser.SentenciaContext): pass
    def exitSentencia(self, ctx: ExprParser.SentenciaContext): pass
    def enterSentencia_if(self, ctx: ExprParser.Sentencia_ifContext): pass
    def exitSentencia_if(self, ctx: ExprParser.Sentencia_ifContext): pass
    def enterSentencia_while(self, ctx: ExprParser.Sentencia_whileContext): pass
    def exitSentencia_while(self, ctx: ExprParser.Sentencia_whileContext): pass
    def enterFuncion_llamada(self, ctx: ExprParser.Funcion_llamadaContext): pass
    def exitFuncion_llamada(self, ctx: ExprParser.Funcion_llamadaContext): pass
    def enterParametros(self, ctx: ExprParser.ParametrosContext): pass
    def exitParametros(self, ctx: ExprParser.ParametrosContext): pass
    def enterParametro(self, ctx: ExprParser.ParametroContext): pass
    def exitParametro(self, ctx: ExprParser.ParametroContext): pass
    def enterArgumentos(self, ctx: ExprParser.ArgumentosContext): pass
    def exitArgumentos(self, ctx: ExprParser.ArgumentosContext): pass
    def enterBloque_de_sentencia(self, ctx: ExprParser.Bloque_de_sentenciaContext): pass
    def exitBloque_de_sentencia(self, ctx: ExprParser.Bloque_de_sentenciaContext): pass
    def enterFactor(self, ctx: ExprParser.FactorContext): pass
    def exitFactor(self, ctx:ExprParser.FactorContext): pass

    # ----------------------- Important Rule Implementations -----------------------

    def enterRetorna(self, ctx: ExprParser.RetornaContext):
        if not self.current_function:
            self.report_error(ctx, "Error: 'retorna' fuera de una función")
            return

        print(f"Procesando 'retorna' en la función '{self.current_function}'")

        expected_type = self.symbol_table.get_function_return_type(self.current_function)
        expr_type = self._get_type_from_node(ctx.expr())

        if expr_type is None:
            expr_type = self._infer_type_from_expression(ctx.expr())

        if expected_type != expr_type:
            self.report_error(ctx, 
                f"Error: La función '{self.current_function}' debe retornar '{expected_type}' " +
                f"pero se encontró '{expr_type if expr_type else 'None'}'")

    def exitRetorna(self, ctx:ExprParser.RetornaContext): pass

    def enterSentencia_for(self, ctx: ExprParser.Sentencia_forContext):
        self.symbol_table.enter_scope()  # Nuevo scope para el for
        
        declaracion = ctx.declaracion()  
        if declaracion:
            tipo = declaracion.tipo().getText()
            nombre_variable = declaracion.VARIABLE().getText()

            if self.symbol_table.get_variable_in_current_scope(nombre_variable):
                self.report_error(ctx, f"Error: La variable '{nombre_variable}' ya ha sido declarada en este scope.")
                return

            self.symbol_table.define_variable(nombre_variable, tipo)


    def exitSentencia_for(self, ctx: ExprParser.Sentencia_forContext):
        self.symbol_table.exit_scope()  # Salir del scope del f

    # En el Listener (corrección para funciones):
    def enterDeclaracion_funcion(self, ctx: ExprParser.Declaracion_funcionContext):
        nombre_funcion = ctx.VARIABLE().getText()
        tipo_retorno = ctx.tipo().getText()

        self.current_function = nombre_funcion  # Establecer la función actual

        params = []
        if ctx.parametros():
            for param in ctx.parametros().parametro():
                param_name = param.VARIABLE().getText()
                param_type = param.tipo().getText()
                if not self._is_valid_identifier(param_name):
                    self.report_error(ctx, f"Error: Nombre de parámetro '{param_name}' no válido en la función '{nombre_funcion}'.")
                if param_name in [p[0] for p in params]:
                    self.report_error(ctx, f"Error: Parámetro duplicado '{param_name}' en la función '{nombre_funcion}'.")
                params.append((param_name, param_type))

        self.symbol_table.define_function(nombre_funcion, params, tipo_retorno)
        self.symbol_table.enter_scope()

        for param_name, param_type in params:
            self.symbol_table.define_variable(param_name, param_type)

    def exitDeclaracion_funcion(self, ctx: ExprParser.Declaracion_funcionContext):
        self.current_function = None 
        self.symbol_table.exit_scope()

    def enterDeclaracion_sin_asignacion(self, ctx:ExprParser.Declaracion_sin_asignacionContext):
        tipo = ctx.tipo().getText()
        if tipo is None:
            print(f"Error: Tipo desconocido '{tipo}' en la declaración.")
            return
        
        variable = ctx.VARIABLE()
        if variable is None:
            print("Error: Variable no encontrada en la declaración.")
            return
        
        nombre_variable = variable.getText()
        if self.symbol_table.get_variable(nombre_variable) is not None:
            print(f"Error: Variable '{nombre_variable}' ya declarada.")
            return
            
        self.report_error(ctx, f"Warning: Variable '{nombre_variable}' declarada pero no instanciada.")
        self.symbol_table.define_variable(nombre_variable, tipo)

    def exitDeclaracion_sin_asignacion(self, ctx:ExprParser.Declaracion_sin_asignacionContext): pass

    def enterFuncion_llamada_expr(self, ctx: ExprParser.Funcion_llamada_exprContext):
        nombre_funcion = ctx.VARIABLE().getText()
        funcion_info = self.symbol_table.get_function(nombre_funcion)

        if funcion_info is None:
            self.report_error(ctx, f"Error: Función '{nombre_funcion}' no definida.")
            return

        parametros = funcion_info['params']
        argumentos = ctx.argumentos().expr() if ctx.argumentos() else []

        if len(argumentos) != len(parametros):
            self.report_error(ctx, f"Error: La función '{nombre_funcion}' espera {len(parametros)} argumentos pero se proporcionaron {len(argumentos)}.")
            return

        for arg, param in zip(argumentos, parametros):
            arg_type = self._infer_type_from_expression(arg)
            param_type = param[1]
            if arg_type != param_type:
                self.report_error(ctx, f"Error: Tipo incompatible en el argumento '{arg.getText()}'. Se esperaba '{param_type}' pero se encontró '{arg_type}'.")

    def exitFuncion_llamada_expr(self, ctx:ExprParser.Funcion_llamada_exprContext): pass

    def enterBloque_condicional(self, ctx: ExprParser.Bloque_condicionalContext):
        self.symbol_table.enter_scope()

    def exitBloque_condicional(self, ctx: ExprParser.Bloque_condicionalContext):
        self.symbol_table.exit_scope()

    def enterDeclaracion(self, ctx: ExprParser.DeclaracionContext):
        tipo = ctx.tipo().getText()
        variable = ctx.VARIABLE()
        nombre_variable = variable.getText()

        if not self._is_valid_identifier(nombre_variable):
            self.report_error(ctx, f"Error: Nombre de variable '{nombre_variable}' no válido.")
            return

        if self.symbol_table.get_variable(nombre_variable) is not None:
            self.report_error(ctx, f"Error: Variable '{nombre_variable}' ya declarada.")
            return

        if ctx.expr():
            expr_type = self._infer_type_from_expression(ctx.expr())
            if expr_type != tipo:
                self.report_error(ctx, f"Error: Tipo incompatible. Se esperaba '{tipo}' pero se encontró '{expr_type}'.")

        self.symbol_table.define_variable(nombre_variable, tipo)

    def exitDeclaracion(self, ctx: ExprParser.DeclaracionContext): pass

    def enterReasignacion(self, ctx: ExprParser.ReasignacionContext):
        nombre_variable = ctx.VARIABLE().getText()
        variable_type = self.symbol_table.get_variable_type(nombre_variable)

        if variable_type is None:
            self.report_error(ctx, f"Error: Variable '{nombre_variable}' no declarada antes de su uso.")
            return

        if ctx.expr():
            expr_type = self._infer_type_from_expression(ctx.expr())
            if expr_type != variable_type:
                self.report_error(ctx, f"Error: Tipo incompatible. La variable '{nombre_variable}' es de tipo '{variable_type}' pero se intentó asignar un valor de tipo '{expr_type}'.")

    def exitReasignacion(self, ctx: ExprParser.ReasignacionContext): pass

    def enterActualizacion(self, ctx: ExprParser.ActualizacionContext):
        nombre_variable = ctx.VARIABLE().getText()
        variable_type = self.symbol_table.get_variable_type(nombre_variable)

        if variable_type is None:
            self.report_error(ctx, f"Error: No se puede actualizar la variable '{nombre_variable}' porque aún no ha sido declarada.")
            return

        if variable_type not in {'entero', 'decimal'}:
            self.report_error(ctx, f"Error: Solo se pueden actualizar variables de tipo numérico ('entero' o 'decimal'). La variable '{nombre_variable}' es de tipo '{variable_type}'.")


    def exitActualizacion(self, ctx:ExprParser.ActualizacionContext): pass

    # ----------------------- Expression Handling -----------------------

    def enterTerm(self, ctx:ExprParser.TermContext):
        if ctx.getChildCount() == 3:
            ctx.type = self._get_type_from_node(ctx)
            print(f"Term result: {ctx.getText()} -> {ctx.type}")
            if ctx.getChildCount() == 3:  # Operación binaria como a * b
                left = ctx.getChild(0)
                operator = ctx.getChild(1).getText()
                right = ctx.getChild(2)

                left_type = self._get_type_from_node(left)
                right_type = self._get_type_from_node(right)
                
                print(f"Term operation: {left.getText()}({left_type}) {operator} {right.getText()}({right_type})")

                if left_type == "no_declarada" or right_type == "no_declarada":
                    undeclared = []
                    if left_type == "no_declarada" and isinstance(left, TerminalNode) and left.getText().isidentifier():
                        undeclared.append(left.getText())
                    if right_type == "no_declarada" and isinstance(right, TerminalNode) and right.getText().isidentifier():
                        undeclared.append(right.getText())
                    if undeclared:
                        self.report_error(ctx, f"Error: Variable(s) no declarada(s) {tuple(undeclared)}")
                    return

                if operator in {'*', '/'}:
                    if not (self._is_numeric_type(left_type) and self._is_numeric_type(right_type)):
                        self.report_error(ctx, f"No se puede aplicar '{operator}' entre '{left_type}' y '{right_type}'")
                        return
                    
                    if 'decimal' in (left_type, right_type) or 'float' in (left_type, right_type):
                        ctx.type = 'decimal'
                    else:
                        ctx.type = 'entero'
                    print(f"Term result type set to: {ctx.type}")
            else:
                factor = ctx.getChild(0)
                ctx.type = self._get_type_from_node(factor)
                print(f"Single term type: {factor.getText()} -> {ctx.type}")

    def exitTerm(self, ctx:ExprParser.TermContext):
        if ctx.getChildCount() == 3:
            left = ctx.getChild(0)
            right = ctx.getChild(2)
            
            left_type = getattr(left, 'type', None) or self._get_type_from_node(left)
            right_type = getattr(right, 'type', None) or self._get_type_from_node(right)
            
            if left_type in {'entero', 'decimal'} and right_type in {'entero', 'decimal'}:
                if left_type == 'decimal' or right_type == 'decimal':
                    ctx.type = 'decimal'
                else:
                    ctx.type = 'entero'

    def enterExpr(self, ctx:ExprParser.ExprContext):
        if ctx.getChildCount() == 3:  # Operación binaria
            left = ctx.getChild(0)
            operator = ctx.getChild(1).getText()
            right = ctx.getChild(2)

            left_type = self._infer_type_from_expression(left)
            right_type = self._infer_type_from_expression(right)

            if operator in ['+', '-', '*', '/']:
                if not (self._is_numeric_type(left_type) and self._is_numeric_type(right_type)):
                    self.report_error(ctx, f"Error: Operación '{operator}' no válida entre '{left_type}' y '{right_type}'.")
            elif operator == '%':
                if left_type != 'entero' or right_type != 'entero':
                    self.report_error(ctx, f"Error: Operación '%' solo válida entre enteros, pero se encontró '{left_type}' y '{right_type}'.")
            elif operator in ['&&', '||']:
                if left_type != 'bool' or right_type != 'bool':
                    self.report_error(ctx, f"Error: Operación lógica '{operator}' solo válida entre booleanos, pero se encontró '{left_type}' y '{right_type}'.")
            elif operator in ['<', '>', '<=', '>=']:
                if not (self._is_numeric_type(left_type) and self._is_numeric_type(right_type)):
                    self.report_error(ctx, f"Error: Operación '{operator}' no válida entre '{left_type}' y '{right_type}'.")
            elif operator in ['==', '!=']:
                if left_type != right_type:
                    self.report_error(ctx, f"Error: Comparación '{operator}' no válida entre '{left_type}' y '{right_type}'.")


    def exitExpr(self, ctx: ExprParser.ExprContext):
        if ctx.getChildCount() == 3:
            left = ctx.getChild(0)
            right = ctx.getChild(2)
            
            left_type = getattr(left, 'type', None) or self._get_operand_type(left.getText())
            right_type = getattr(right, 'type', None) or self._get_operand_type(right.getText())
            
            if left_type in {'entero', 'decimal'} and right_type in {'entero', 'decimal'}:
                if left_type == 'decimal' or right_type == 'decimal':
                    ctx.type = 'decimal'
                else:
                    ctx.type = 'entero'

    # ----------------------- Utility Methods -----------------------

    def enterScope(self):
        """Crear un nuevo ámbito (nuevo diccionario en la pila)."""
        self.symbol_table.enter_scope()

    def exitScope(self):
        """Eliminar el último ámbito (salir del bloque actual)."""
        self.symbol_table.exit_scope()

    def panic(self):
        if self.panic_mode:
            print("Modo pánico activado, intentando continuar la ejecución...")
            self.panic_mode = False

    def traducir_tipo(self, tipo):
        tipos = {"int": "entero", "float": "decimal", "str": "cadena", "bool": "bool"}
        return tipos.get(tipo, None)

    def _is_numeric_type(self, type_str):
        """Verifica si el tipo es numérico (entero o decimal)"""
        return type_str in {'entero', 'decimal', 'int', 'float', 'cadena','str'}

    def _determine_literal_type(self, value):
        """Determina el tipo de un literal"""
        if value.isdigit():
            return 'entero'
        try:
            float(value)
            return 'decimal' if '.' in value else 'entero'
        except ValueError:
            if (value.startswith('"') and value.endswith('"')) or \
               (value.startswith("'") and value.endswith("'")):
                return 'cadena'
            elif value.lower() in {'verdadero', 'falso'}:
                return 'bool'
        return 'desconocido'    

    def limpiar_cadena(self, cadena):
        """Limpia una cadena reemplazando caracteres inválidos"""
        caracteres_permitidos = self.letras + self.digitos + " .,;:!?¿¡-_"
        return ''.join(c if c in caracteres_permitidos else '.' for c in cadena)

    def _get_operand_type(self, operand_name):
        """Determines the type of an operand (variable, literal, or function call)"""
        try:
            # Handle function calls
            if '(' in operand_name and operand_name.endswith(')'):
                func_name = operand_name.split('(')[0]
                return self.symbol_table.get_function_return_type(func_name) or "desconocido"
            
            # Handle parenthesized expressions
            if operand_name.startswith('(') and operand_name.endswith(')'):
                return self._determine_literal_type(operand_name[1:-1])
                
            # Handle variables
            if operand_name.isidentifier():
                var_info = self.symbol_table.get_variable(operand_name)
                if var_info is None:
                    return "no_declarada"
                # Normalize types
                if var_info == 'int':
                    return 'entero'
                elif var_info == 'float':
                    return 'decimal'
                return var_info
                
            # Handle literals
            return self._determine_literal_type(operand_name)
        except Exception as e:
            print(f"Error en _get_operand_type: {str(e)}")
            return "desconocido"

    def _validate_operation(self, left_type, right_type, operator):
        valid_combinations = {
            '+': [{'entero', 'decimal'}, {'entero', 'decimal'}],
            '-': [{'entero', 'decimal'}, {'entero', 'decimal'}],
            '*': [{'entero', 'decimal'}, {'entero', 'decimal'}],
            '/': [{'entero', 'decimal'}, {'entero', 'decimal'}],
            '%': [{'entero'}, {'entero'}],
            '^': [{'entero', 'decimal'}, {'entero', 'decimal'}],
        }
        if operator not in valid_combinations:
            return False
        allowed_left, allowed_right = valid_combinations[operator]
        return left_type in allowed_left and right_type in allowed_right

    def _validate_comparison(self, left_type, right_type, operator):
        """Validates that the types are comparable"""
        if operator in {'<', '>', '<=', '>='}:
            return self._is_numeric_type(left_type) and self._is_numeric_type(right_type)
        elif operator in {'==', '!='}:
            return left_type == right_type
        return False

    def _get_type_from_node(self, node):
        if node is None:
            return None
        
        # Si el nodo ya tiene tipo asignado
        if hasattr(node, 'type'):
            return node.type

        text = node.getText()

        # Literales
        if text.isdigit():
            return 'entero'
        elif text.replace('.', '', 1).isdigit():
            return 'decimal'
        elif text.startswith('"') and text.endswith('"'):
            return 'cadena'
        elif text in ['verdadero', 'falso']:
            return 'bool'
        
        # Llamadas a funciones
        if '(' in text and text.endswith(')'):
            func_name = text.split('(')[0]
            return self.symbol_table.get_function_return_type(func_name)
        
        # Variables
        var_type = self.symbol_table.get_variable(text)
        if var_type:
            return var_type

        return None

    def _infer_type_from_expression(self, expr_node):
        if isinstance(expr_node, TerminalNode):
            return self._get_type_from_node(expr_node)
        
        if hasattr(expr_node, 'type'):
            return expr_node.type
        
        if expr_node.getChildCount() == 1:
            return self._infer_type_from_expression(expr_node.getChild(0))
        
        if expr_node.getChildCount() == 3:  # Operación binaria
            left_type = self._infer_type_from_expression(expr_node.getChild(0))
            right_type = self._infer_type_from_expression(expr_node.getChild(2))
            operator = expr_node.getChild(1).getText()
            
            if operator in ['+', '-', '*', '/']:
                if 'decimal' in (left_type, right_type):
                    return 'decimal'
                if 'entero' in (left_type, right_type):
                    return 'entero'
                self.report_error(expr_node, f"Operación '{operator}' no válida entre {left_type} y {right_type}")
            elif operator in ['==', '!=', '<', '>', '<=', '>=']:
                return 'bool'
            elif operator == '%':
                if left_type == 'entero' and right_type == 'entero':
                    return 'entero'
                self.report_error(expr_node, f"Operación '%' no válida entre {left_type} y {right_type}")
            elif operator == '^':
                if self._is_numeric_type(left_type) and self._is_numeric_type(right_type):
                    return 'decimal' if 'decimal' in (left_type, right_type) else 'entero'
                self.report_error(expr_node, f"Operación '^' no válida entre {left_type} y {right_type}")
    
        # Manejar llamadas a funciones
        if expr_node.getChildCount() > 0 and expr_node.getChild(0).getText().isidentifier():
            func_name = expr_node.getChild(0).getText()
            return self.symbol_table.get_function_return_type(func_name) or "desconocido"
    
        return None

    def _infer_function_return_type(self, node):
        """Infers the return type of a function call node"""
        if isinstance(node, TerminalNode):
            text = node.getText()
            if '(' in text and text.endswith(')'):
                func_name = text.split('(')[0]
                return self.symbol_table.get_function_return_type(func_name)
        return "desconocido"

    def validar_cadena_valida(self, cadena: str):
        """Valida que la cadena contenga al menos un carácter válido"""
        caracteres_validos = self.letras + self.digitos + " .,;:!?¿¡-_@#$%&()"
        return any(c in caracteres_validos for c in cadena)

    def report_error(self, ctx, message):
        line = ctx.start.line if ctx.start else "unknown"
        col = ctx.start.column
        print(f"Error en línea {line}, columna {col}: {message}")
        print(f"Contexto: {ctx.getText()}")
        exit(1)
        
    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        pass

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        pass

    def enterSentencia_switch(self, ctx: ExprParser.Sentencia_switchContext):
        """Maneja la entrada a una sentencia switch."""
        expr_type = self._infer_type_from_expression(ctx.expr())
        if expr_type not in {'entero', 'cadena', 'bool'}:
            self.report_error(ctx, f"Error: El tipo de la expresión en 'switch' debe ser 'entero', 'cadena' o 'bool', pero se encontró '{expr_type}'.")

    def exitSentencia_switch(self, ctx: ExprParser.Sentencia_switchContext):
        """Maneja la salida de una sentencia switch."""
        print(f"Salida de sentencia switch con expresión: {ctx.expr().getText()}")

    def enterMostrar(self, ctx: ExprParser.MostrarContext):
        """Maneja la entrada a una sentencia mostrar."""
        expr_type = self._infer_type_from_expression(ctx.expr())
        if expr_type is None:
            self.report_error(ctx, "Error: No se puede determinar el tipo de la expresión en 'mostrar'.")
        else:
            print(f"Mostrando expresión de tipo: {expr_type}")

    def exitMostrar(self, ctx: ExprParser.MostrarContext):
        """Maneja la salida de una sentencia mostrar."""
        print(f"Salida de sentencia mostrar con expresión: {ctx.expr().getText()}")

    def _validate_literal(self, literal):
        """Valida que un literal sea válido."""
        if literal.isdigit():
            return True  # Es un número entero válido
        try:
            float(literal)
            return True  # Es un número decimal válido
        except ValueError:
            pass
        if (literal.startswith('"') and literal.endswith('"')) or \
           (literal.startswith("'") and literal.endswith("'")):
            return True  # Es una cadena válida
        if literal.lower() in {'verdadero', 'falso'}:
            return True  # Es un booleano válido
        return False

    def enterFactor(self, ctx: ExprParser.FactorContext):
        if ctx.NUMERO() or ctx.DECIMAL() or ctx.CADENA() or ctx.BOOLEANO():
            literal = ctx.getText()
            if not self._validate_literal(literal):
                self.report_error(ctx, f"Error: Literal no válido '{literal}'.")
        if ctx.CADENA():
            cadena = ctx.getText()
            if not self.validar_cadena_valida(cadena):
                self.report_error(ctx, f"Error: La cadena '{cadena}' contiene caracteres no válidos.")

    def _is_valid_identifier(self, name):
        """Verifica si un identificador es válido según las reglas del lenguaje."""
        if not name:
            return False  # El identificador no puede estar vacío
        if name[0] not in self.letras:  # Debe comenzar con una letra o un guion bajo
            return False
        for char in name:
            if char not in self.letras + self.digitos + "_":  # Solo se permiten letras, dígitos y guiones bajos
                return False
        return True