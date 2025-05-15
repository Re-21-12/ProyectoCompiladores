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
    def enterFactor(self, ctx:ExprParser.FactorContext): pass
    def exitFactor(self, ctx:ExprParser.FactorContext): pass

    # ----------------------- Important Rule Implementations -----------------------

    def enterRetorna(self, ctx: ExprParser.RetornaContext):
        if not self.current_function:
            self.report_error(ctx, "Error: 'retorna' fuera de una función")
            return
        
        expected_type = self.symbol_table.get_function_return_type(self.current_function)
        actual_type = self._get_type_from_node(ctx.expr())
        
        if expected_type != actual_type:
            self.report_error(ctx, f"Error: La función '{self.current_function}' debe retornar '{expected_type}' pero se encontró '{actual_type}'")

    def exitRetorna(self, ctx:ExprParser.RetornaContext): pass

    def enterSentencia_for(self, ctx: ExprParser.Sentencia_forContext):
        declaracion = ctx.declaracion()  
        if declaracion:
            tipo = declaracion.tipo().getText()
            nombre_variable = declaracion.VARIABLE().getText()

            if self.symbol_table.get_variable(nombre_variable):
                self.report_error(ctx, f"Error: La variable '{nombre_variable}' ya ha sido declarada.")
                return

            self.symbol_table.define_variable(nombre_variable, tipo)
        else:
            self.report_error(ctx, "Error: No se ha declarado una variable de iteración en el for.")

    def exitSentencia_for(self, ctx: ExprParser.Sentencia_forContext): pass

    def enterDeclaracion_funcion(self, ctx: ExprParser.Declaracion_funcionContext):
        nombre_funcion = ctx.VARIABLE().getText()
        self.current_function = nombre_funcion
        tipo_retorno = ctx.tipo().getText()
        
        params = []
        if ctx.parametros():
            for param in ctx.parametros().parametro():
                param_name = param.VARIABLE().getText()
                param_type = param.tipo().getText()
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
        
        if not self.symbol_table.get_function_return_type(nombre_funcion):
            self.report_error(ctx, f"Error: Función '{nombre_funcion}' no definida")
            return
        
        return_type = self.symbol_table.get_function_return_type(nombre_funcion)
        ctx.type = return_type
        print(f"Llamada a función '{nombre_funcion}' retorna: {return_type}")

    def exitFuncion_llamada_expr(self, ctx:ExprParser.Funcion_llamada_exprContext): pass

    def enterBloque_condicional(self, ctx: ExprParser.Bloque_condicionalContext):
        self.symbol_table.enter_scope()

    def exitBloque_condicional(self, ctx: ExprParser.Bloque_condicionalContext):
        self.symbol_table.exit_scope()

    def enterDeclaracion(self, ctx: ExprParser.DeclaracionContext):
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
        
        if ctx.ASIGNACION() and tipo is None:
            self.report_error(ctx, f"Error: No se pudo determinar el tipo de la expresión en la asignación de '{nombre_variable}'.")
            return

        self.symbol_table.define_variable(nombre_variable, tipo)

    def exitDeclaracion(self, ctx: ExprParser.DeclaracionContext): pass

    def enterReasignacion(self, ctx: ExprParser.ReasignacionContext):
        nombre_variable = ctx.VARIABLE().getText()
        print(f'[WARN]: Reasignando variable {nombre_variable}')
        if self.symbol_table.get_variable(nombre_variable) is None:
            self.report_error(ctx,f"Error: Variable '{nombre_variable}' no declarada antes de su uso.")
            return
        if ctx.expr():
            valor = ctx.expr().getText()
            if (valor.startswith('"') and valor.endswith('"')) or (valor.startswith("'") and valor.endswith("'")):
                contenido = valor.strip('"\'').strip()
                if not self.validar_cadena_valida(contenido):
                    corregido = self.limpiar_cadena(contenido)
                    self.report_error(ctx, f"Advertencia: La cadena '{contenido}' contiene caracteres no válidos. Se corrigió a '{corregido}'")

    def exitReasignacion(self, ctx: ExprParser.ReasignacionContext): pass

    def enterActualizacion(self, ctx: ExprParser.ActualizacionContext):
        nombre_variable = ctx.VARIABLE().getText()
        tipo = self.symbol_table.get_variable_type(nombre_variable)
        
        print(f"[WARN] Actualizando variable: {nombre_variable}")
        print(tipo)
        if tipo is None:
            self.report_error(ctx, f"Error: No se puede actualizar la variable '{nombre_variable}' porque aún no ha sido declarada")
            return

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
        if ctx.getChildCount() == 3:
            ctx.type = self._get_type_from_node(ctx)
            print(f"Expr result: {ctx.getText()} -> {ctx.type}")
        
        if ctx.getChildCount() == 3:
            left = ctx.getChild(0)
            operator = ctx.getChild(1).getText()
            right = ctx.getChild(2)

            left_type = self._get_type_from_node(left)
            right_type = self._get_type_from_node(right)
            
            print(f"Expr operation: {left.getText()}({left_type}) {operator} {right.getText()}({right_type})")

            if left_type == "desconocido":
                left_type = self._infer_function_return_type(left)
            if right_type == "desconocido":
                right_type = self._infer_function_return_type(right)    

            if left_type == "no_declarada" or right_type == "no_declarada":
                undeclared = []
                if left_type == "no_declarada" and isinstance(left, TerminalNode) and left.getText().isidentifier():
                    undeclared.append(left.getText())
                if right_type == "no_declarada" and isinstance(right, TerminalNode) and right.getText().isidentifier():
                    undeclared.append(right.getText())
                if undeclared:
                    self.report_error(ctx, f"Error: Variable(s) no declarada(s) {tuple(undeclared)}")
                return

            if operator == '+':
                if left_type == 'cadena' and right_type == 'cadena':
                    ctx.type = 'cadena'
                    print(f"Concatenación result: {ctx.type}")
                    return
                    
                if not (self._is_numeric_type(left_type) and self._is_numeric_type(right_type)):
                    self.report_error(ctx, f"No se puede aplicar '{operator}' entre '{left_type}' y '{right_type}'")
                    return
            
            if operator in {'+', '-'}:
                if not (self._is_numeric_type(left_type) and self._is_numeric_type(right_type)):
                    self.report_error(ctx, f"No se puede aplicar '{operator}' entre '{left_type}' y '{right_type}'")
                    return
                
                if 'decimal' in (left_type, right_type) or 'float' in (left_type, right_type):
                    ctx.type = 'decimal'
                else:
                    ctx.type = 'entero'
                print(f"Expr result type set to: {ctx.type}")

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
            '*': [{'entero', 'decimal'}, {'entero', 'decimal'}],
            '==': [{'entero', 'decimal', 'bool', 'cadena'}, {'entero', 'decimal', 'bool', 'cadena'}]
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
        """Versión mejorada que maneja operaciones anidadas"""
        if isinstance(node, ParserRuleContext):
            if node.getChildCount() == 3:
                left = self._get_type_from_node(node.getChild(0))
                right = self._get_type_from_node(node.getChild(2))
                
                if left == "no_declarada" or right == "no_declarada":
                    return "no_declarada"
                    
                if not (self._is_numeric_type(left) and self._is_numeric_type(right)):
                    return "desconocido"
                
                return 'decimal' if 'decimal' in (left, right) else 'entero'
        return self._get_operand_type(node.getText())

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