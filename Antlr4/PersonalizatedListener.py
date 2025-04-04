import SymbolTable
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser
from ExprListener import ExprListener
from SymbolTable import SymbolTable
# This class defines a complete listener for a parse tree produced by ExprParser.
class PersonalizatedListener(ExprListener, SymbolTable):
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.panic_mode = False  # Control para el modo pánico

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
            # Aquí puedes manejar el error a tu manera, por ejemplo, imprimir el error
            print(f"Error de sintaxis en la línea {line}, columna {column}: {msg}")
            # Si deseas, puedes incluso lanzar una excepción o realizar alguna acción personalizada

    # Enter a parse tree produced by ExprParser#gramatica.
    def enterGramatica(self, ctx: ExprParser.GramaticaContext):
        pass

    # Exit a parse tree produced by ExprParser#gramatica.
    def exitGramatica(self, ctx: ExprParser.GramaticaContext):
        pass

    # Enter a parse tree produced by ExprParser#programa.
    def enterPrograma(self, ctx: ExprParser.ProgramaContext):
        pass

    # Exit a parse tree produced by ExprParser#programa.
    def exitPrograma(self, ctx: ExprParser.ProgramaContext):
        pass

    # Enter a parse tree produced by ExprParser#bloque.
    def enterBloque(self, ctx: ExprParser.BloqueContext):
        pass

    # Exit a parse tree produced by ExprParser#bloque.
    def exitBloque(self, ctx: ExprParser.BloqueContext):
        pass

    # Enter a parse tree produced by ExprParser#sentencia.
    def enterSentencia(self, ctx: ExprParser.SentenciaContext):
        pass

    # Exit a parse tree produced by ExprParser#sentencia.
    def exitSentencia(self, ctx: ExprParser.SentenciaContext):
        pass

    # Enter a parse tree produced by ExprParser#sentencia_if.
    def enterSentencia_if(self, ctx: ExprParser.Sentencia_ifContext):
        pass

    # Exit a parse tree produced by ExprParser#sentencia_if.
    def exitSentencia_if(self, ctx: ExprParser.Sentencia_ifContext):
        pass

    # Enter a parse tree produced by ExprParser#sentencia_while.
    def enterSentencia_while(self, ctx: ExprParser.Sentencia_whileContext):
        pass

    # Exit a parse tree produced by ExprParser#sentencia_while.
    def exitSentencia_while(self, ctx: ExprParser.Sentencia_whileContext):
        pass

    # Enter a parse tree produced by ExprParser#sentencia_for.
    def enterSentencia_for(self, ctx: ExprParser.Sentencia_forContext):
        declaracion = ctx.declaracion()  
        
        if declaracion:
            tipo = declaracion.tipo().getText()
            nombre_variable = declaracion.VARIABLE().getText()

            # Verificar si la variable ya está declarada
            if self.symbol_table.get_variable(nombre_variable):
                self.report_error(ctx, f"Error: La variable '{nombre_variable}' ya ha sido declarada.")
                return

            # Registrar la variable en la tabla de símbolos
            self.symbol_table.define_variable(nombre_variable, tipo)
        else:
            self.report_error(ctx, "Error: No se ha declarado una variable de iteración en el for.")

    # Exit a parse tree produced by ExprParser#sentencia_for.
    def exitSentencia_for(self, ctx: ExprParser.Sentencia_forContext):
        pass

    # Al entrar a una función, creamos un nuevo ámbito
    def enterDeclaracion_funcion(self, ctx: ExprParser.Declaracion_funcionContext):
        # Ingresamos al ámbito de la función
        self.symbol_table.enter_scope()

        # Revisamos si existen parámetros
        if ctx.parametros():
            # Extraemos los parámetros y los agregamos a la tabla de símbolos
            for param in ctx.parametros().parametro():
                param_name = param.VARIABLE().getText()  # Nombre del parámetro
                param_type = param.tipo().getText()  # Tipo del parámetro (dependiendo de la gramática)
                
                # Aquí agregamos el parámetro al símbolo con el tipo adecuado
                self.symbol_table.define_variable(param_name, param_type)

    # Al salir de una función, salimos del ámbito
    def exitDeclaracion_funcion(self, ctx: ExprParser.Declaracion_funcionContext):
        self.symbol_table.exit_scope()

    # Enter a parse tree produced by ExprParser#funcion_llamada.
    def enterFuncion_llamada(self, ctx: ExprParser.Funcion_llamadaContext):
        pass

    # Exit a parse tree produced by ExprParser#funcion_llamada.
    def exitFuncion_llamada(self, ctx: ExprParser.Funcion_llamadaContext):
        pass

    # Enter a parse tree produced by ExprParser#parametros.
    def enterParametros(self, ctx: ExprParser.ParametrosContext):
        pass

    # Exit a parse tree produced by ExprParser#parametros.
    def exitParametros(self, ctx: ExprParser.ParametrosContext):
        pass

    # Enter a parse tree produced by ExprParser#parametro.
    def enterParametro(self, ctx: ExprParser.ParametroContext):
        pass

    # Exit a parse tree produced by ExprParser#parametro.
    def exitParametro(self, ctx: ExprParser.ParametroContext):
        pass

    # Enter a parse tree produced by ExprParser#argumentos.
    def enterArgumentos(self, ctx: ExprParser.ArgumentosContext):
        pass

    # Exit a parse tree produced by ExprParser#argumentos.
    def exitArgumentos(self, ctx: ExprParser.ArgumentosContext):
        pass
    # Enter a parse tree produced by ExprParser#bloque_condicional.
    def enterBloque_condicional(self, ctx: ExprParser.Bloque_condicionalContext):
        self.symbol_table.enter_scope()

    # Exit a parse tree produced by ExprParser#bloque_condicional.
    def exitBloque_condicional(self, ctx: ExprParser.Bloque_condicionalContext):
        self.symbol_table.exit_scope()

    # Enter a parse tree produced by ExprParser#bloque_de_sentencia.
    def enterBloque_de_sentencia(self, ctx: ExprParser.Bloque_de_sentenciaContext):
        pass

    # Exit a parse tree produced by ExprParser#bloque_de_sentencia.
    def exitBloque_de_sentencia(self, ctx: ExprParser.Bloque_de_sentenciaContext):
        pass

    # Enter a parse tree produced by ExprParser#declaracion.
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
        
        # Validar asignación si existe
        if ctx.ASIGNACION():
            
            if tipo is None:
                self.report_error(ctx, f"Error: No se pudo determinar el tipo de la expresión en la asignación de '{nombre_variable}'.")
                return


        self.symbol_table.define_variable(nombre_variable, tipo)

    # Exit a parse tree produced by ExprParser#declaracion.
    def exitDeclaracion(self, ctx: ExprParser.DeclaracionContext):
        pass

    # Cuando entras a una asignación
    def enterReasignacion(self, ctx: ExprParser.ReasignacionContext):
        nombre_variable = ctx.VARIABLE().getText()
        print(f'[WARN]: Reasignando variable {nombre_variable}')
        if self.symbol_table.get_variable(nombre_variable) is None:
            self.report_error(ctx,f"Error: Variable '{nombre_variable}' no declarada antes de su uso.")
            return
  
    # Exit a parse tree produced by ExprParser#reasignacion.
    def exitReasignacion(self, ctx: ExprParser.ReasignacionContext):
        pass

    def enterTerm(self, ctx:ExprParser.TermContext):
        if ctx.getChildCount() == 3:
            ctx.type = self._get_type_from_node(ctx)
            print(f"Term result: {ctx.getText()} -> {ctx.type}")
            if ctx.getChildCount() == 3:  # Operación binaria como a * b
                left = ctx.getChild(0)
                operator = ctx.getChild(1).getText()
                right = ctx.getChild(2)

                # Obtenemos los tipos de los operandos individualmente
                left_type = self._get_type_from_node(left)
                right_type = self._get_type_from_node(right)
                
                print(f"Term operation: {left.getText()}({left_type}) {operator} {right.getText()}({right_type})")

                # Verificación de variables no declaradas
                if left_type == "no_declarada" or right_type == "no_declarada":
                    undeclared = []
                    if left_type == "no_declarada" and isinstance(left, TerminalNode) and left.getText().isidentifier():
                        undeclared.append(left.getText())
                    if right_type == "no_declarada" and isinstance(right, TerminalNode) and right.getText().isidentifier():
                        undeclared.append(right.getText())
                    if undeclared:
                        self.report_error(ctx, f"Error: Variable(s) no declarada(s) {tuple(undeclared)}")
                    return

                # Validación de tipos para operaciones aritméticas
                if operator in {'*', '/'}:
                    if not (self._is_numeric_type(left_type) and self._is_numeric_type(right_type)):
                        self.report_error(ctx, f"No se puede aplicar '{operator}' entre '{left_type}' y '{right_type}'")
                        return
                    
                    # Establecer el tipo resultante
                    if 'decimal' in (left_type, right_type) or 'float' in (left_type, right_type):
                        ctx.type = 'decimal'
                    else:
                        ctx.type = 'entero'
                    print(f"Term result type set to: {ctx.type}")
            else:
                # Manejar términos simples (variables o literales)
                factor = ctx.getChild(0)
                ctx.type = self._get_type_from_node(factor)
                print(f"Single term type: {factor.getText()} -> {ctx.type}")

    def exitTerm(self, ctx:ExprParser.TermContext):
        if ctx.getChildCount() == 3:  # If it's a multiplication/division operation
            left = ctx.getChild(0)
            right = ctx.getChild(2)
            
            left_type = getattr(left, 'type', None) or self._get_type_from_node(left)
            right_type = getattr(right, 'type', None) or self._get_type_from_node(right)
            
            # Set the result type
            if left_type in {'entero', 'decimal'} and right_type in {'entero', 'decimal'}:
                if left_type == 'decimal' or right_type == 'decimal':
                    ctx.type = 'decimal'
                else:
                    ctx.type = 'entero'


    def enterExpr(self, ctx:ExprParser.ExprContext):
        if ctx.getChildCount() == 3:
            ctx.type = self._get_type_from_node(ctx)
            print(f"Expr result: {ctx.getText()} -> {ctx.type}")
        
        # Solo procesamos operaciones binarias (con 3 hijos: izquierda, operador, derecha)
        if ctx.getChildCount() == 3:
            left = ctx.getChild(0)
            operator = ctx.getChild(1).getText()
            right = ctx.getChild(2)

            # Obtenemos los tipos de los operandos (ya procesados en enterTerm)
            left_type = self._get_type_from_node(left)
            right_type = self._get_type_from_node(right)
            
            print(f"Expr operation: {left.getText()}({left_type}) {operator} {right.getText()}({right_type})")

            # Verificación de variables no declaradas
            if left_type == "no_declarada" or right_type == "no_declarada":
                undeclared = []
                if left_type == "no_declarada" and isinstance(left, TerminalNode) and left.getText().isidentifier():
                    undeclared.append(left.getText())
                if right_type == "no_declarada" and isinstance(right, TerminalNode) and right.getText().isidentifier():
                    undeclared.append(right.getText())
                if undeclared:
                    self.report_error(ctx, f"Error: Variable(s) no declarada(s) {tuple(undeclared)}")
                return

            # Validación de tipos para operaciones aritméticas
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
                
                # Establecer el tipo resultante
                if 'decimal' in (left_type, right_type) or 'float' in (left_type, right_type):
                    ctx.type = 'decimal'
                else:
                    ctx.type = 'entero'
                print(f"Expr result type set to: {ctx.type}")

    def exitExpr(self, ctx: ExprParser.ExprContext):
        if ctx.getChildCount() == 3:  # Binary operation
            left = ctx.getChild(0)
            right = ctx.getChild(2)
            
            left_type = getattr(left, 'type', None) or self._get_operand_type(left.getText())
            right_type = getattr(right, 'type', None) or self._get_operand_type(right.getText())
            
            # Set the result type for the expression
            if left_type in {'entero', 'decimal'} and right_type in {'entero', 'decimal'}:
                if left_type == 'decimal' or right_type == 'decimal':
                    ctx.type = 'decimal'
                else:
                    ctx.type = 'entero'


    def _get_operand_type(self, operand_name):
        """Versión más robusta"""
        try:
            if operand_name.startswith('(') and operand_name.endswith(')'):
                return self._determine_literal_type(operand_name[1:-1])
                
            if operand_name.isidentifier():
                var_info = self.symbol_table.get_variable(operand_name)
                if var_info is None:
                    return "no_declarada"
                return 'entero' if var_info == 'int' else 'decimal' if var_info == 'float' else var_info
                
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

    # Enter a parse tree produced by ExprParser#factor.
    def enterFactor(self, ctx:ExprParser.FactorContext):
        pass

    # Exit a parse tree produced by ExprParser#factor.
    def exitFactor(self, ctx:ExprParser.FactorContext):
        pass
    
    # Enter a parse tree produced by ExprParser#actualizacion.
    def enterActualizacion(self, ctx: ExprParser.ActualizacionContext):
        nombre_variable = ctx.VARIABLE().getText()
        tipo = self.symbol_table.get_variable_type(nombre_variable)
        # valor_variable = self.symbol_table.get_variable(nombre_variable)
        print(f"[WARN] Actualizando variable: {nombre_variable}")
        print(tipo)
        if tipo is None:
            self.report_error(ctx, f"Error: No se puede actualizar la variable '{nombre_variable}' porque aún no ha sido declarada")
            return

    # Aquí puedes continuar con la actualización porque `valor_variable` es un número
       

    # Exit a parse tree produced by ExprParser#actualizacion.
    def exitActualizacion(self, ctx:ExprParser.ActualizacionContext):
        pass
    # Control de los alcances (scopes) y validación de variables
    def enterScope(self):
        """Crear un nuevo ámbito (nuevo diccionario en la pila)."""
        self.symbol_table.enter_scope()

    def exitScope(self):
        """Eliminar el último ámbito (salir del bloque actual)."""
        self.symbol_table.exit_scope()

    # Modo pánico: Si ocurre un error, intentar recuperar y continuar el análisis
    def panic(self):
        if self.panic_mode:
            print("Modo pánico activado, intentando continuar la ejecución...")
            self.panic_mode = False  # Desactivar el modo pánico después de la recuperación

    def traducir_tipo(self, tipo):
        tipos = {"int": "entero", "float": "decimal", "str": "cadena", "bool": "bool"}
        return tipos.get(tipo, None)

    def _is_numeric_type(self, type_str):
        """Verifica si el tipo es numérico (entero o decimal)"""
        return type_str in {'entero', 'decimal', 'int', 'float', 'cadena','str'}

    def _get_operand_type(self, operand_name):
        """Determina el tipo de un operando (variable o literal)"""

        print(f"375: {operand_name}")

        if operand_name.startswith('(') and operand_name.endswith(')'):
            # Es una expresión entre paréntesis, extraer el contenido
            inner_expr = operand_name[1:-1]
            return self._determine_literal_type(inner_expr)
        
        if operand_name.isidentifier():
            # Es una variable - buscar en tabla de símbolos
            var_info = self.symbol_table.get_variable(operand_name)
            if var_info is None:
                return "no_declarada"
            # Normalizar tipos
            if var_info == 'int':
                return 'entero'
            elif var_info == 'float':
                return 'decimal'
            return var_info
        else:
            # Es un literal - determinar su tipo
            return self._determine_literal_type(operand_name) 

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
    
    def _get_type_from_node(self, node):
        """Versión mejorada que maneja operaciones anidadas"""
        # Si es una operación (expr o term), evaluamos recursivamente
        if isinstance(node, ParserRuleContext):
            if node.getChildCount() == 3:  # Operación binaria
                left = self._get_type_from_node(node.getChild(0))
                right = self._get_type_from_node(node.getChild(2))
                
                # Solo continuar si ambos operandos son válidos
                if left == "no_declarada" or right == "no_declarada":
                    return "no_declarada"
                    
                if not (self._is_numeric_type(left) and self._is_numeric_type(right)):
                    return "desconocido"
                
                return 'decimal' if 'decimal' in (left, right) else 'entero'
        
        # Para nodos terminales
        return self._get_operand_type(node.getText())

    def report_error(self, ctx, message):
        line = ctx.start.line if ctx.start else "unknown"
        col = ctx.start.column
        print(f"Error en línea {line}, columna {col}: {message}")
        print(f"Contexto: {ctx.getText()}")
        exit(1)
        
    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        pass  # Puedes imprimir un mensaje si lo deseas, pero dejarlo vacío evita el error.

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        pass  # Lo mismo aquí, si quieres registrar algo, usa print()

