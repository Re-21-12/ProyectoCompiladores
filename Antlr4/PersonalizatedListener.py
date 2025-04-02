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



    def _get_operand_type(self, operand_name):
            """Determina el tipo de un operando (variable o literal)"""
            if operand_name.isidentifier():
                # Es una variable - buscar en tabla de símbolos
                var_type = self.symbol_table.get_variable_type(operand_name)
                return var_type if var_type is not None else "no_declarada"
            else:
                # Es un literal - determinar su tipo
                return self._determine_literal_type(operand_name)        

    def _determine_literal_type(self, value):
            """Determina el tipo de un literal"""
            if value.isdigit():
                return 'entero'
            try:
                float(value)
                return 'decimal'
            except ValueError:
                if (value.startswith('"') and value.endswith('"')) or \
                (value.startswith("'") and value.endswith("'")):
                    return 'cadena'
                elif value.lower() in {'verdadero', 'falso'}:
                    return 'bool'
            return 'desconocido'
        
    def enterExpr(self, ctx: ExprParser.ExprContext):
        if ctx.getChildCount() == 3:  # Expresión binaria (ej: a + b)
            left = ctx.getChild(0)
            operator = ctx.getChild(1).getText()
            right = ctx.getChild(2)

            left_name = left.getText()
            right_name = right.getText()

            # Determinar tipos (variables y literales)
            left_type = self._get_operand_type(left_name)
            right_type = self._get_operand_type(right_name)

            # Verificar si hay variables no declaradas
            if left_type == "no_declarada" or right_type == "no_declarada":
                undeclared = []
                if left_type == "no_declarada" and left_name.isidentifier():
                    undeclared.append(left_name)
                if right_type == "no_declarada" and right_name.isidentifier():
                    undeclared.append(right_name)
                self.report_error(ctx, f"Error: Variable(s) no declarada(s) {tuple(undeclared)} en la expresión '{left_name} {operator} {right_name}'")
                self.panic_mode = True
                return

            # Reglas de validación de tipos
            if operator in {'+', '-'}:
                # Operaciones aritméticas
                if left_type in {'entero', 'decimal'} and right_type in {'entero', 'decimal'}:
                    pass  # Operación válida
                elif operator == '+' and left_type == 'cadena' and right_type == 'cadena':
                    pass  # Concatenación de cadenas válida
                else:
                    self.report_error(ctx, f"No se puede aplicar '{operator}' entre '{left_type}' y '{right_type}'")
                    self.panic_mode = True

            elif operator in {'==', '!=', '<', '>', '<=', '>='}:
                # Operaciones de comparación
                if left_type == right_type and left_type in {'entero', 'decimal'}:
                    pass  # Comparación válida (números)
                elif operator in {'==', '!='} and left_type == right_type:
                    pass  # Comparación de igualdad válida para cualquier tipo igual
                else:
                    self.report_error(ctx, f"Comparación inválida entre '{left_type}' y '{right_type}'")
                    self.panic_mode = True
                    
    # Exit a parse tree produced by ExprParser#expr.
    def exitExpr(self, ctx: ExprParser.ExprContext):
        pass

    def enterTerm(self, ctx:ExprParser.TermContext):
          if ctx.getChildCount() == 3:  # Expresión binaria (ej: a * b)
            left = ctx.getChild(0)
            operator = ctx.getChild(1).getText()
            right = ctx.getChild(2)

            left_name = left.getText()
            right_name = right.getText()
            print(left_name)
            print(right_name)
            
            left_type = self.symbol_table.get_variable_type(left_name)
            right_type = self.symbol_table.get_variable_type(right_name)
            print(left_type)
            print(right_type)
            
            if left_type and right_type not in {"entero", "decimal"}:
                self.report_error(ctx,f"Error: Variable no declarada {left_name, right_name} en la expresión '{left_name} {operator} {right_name}'")
                self.panic_mode = True
                return

            # Reglas de validación de tipos
            if operator in {'*', '/', "+", "-"}:
                if left_type in {'entero', 'entero'} and right_type in {'entero', 'entero'}:
                    pass  # Operación válida
                elif left_type in {'decimal', 'decimal'} and right_type in {'decimal', 'decimal'}:
                    pass  # Operación válida
                elif operator == '+' and left_type == 'cadena' and right_type == 'cadena':
                    pass  # Concatenación de cadenas es válida
                else:
                    self.report_error(ctx, f"No se puede aplicar '{operator}' entre '{left_type}' y '{right_type}'")
                    self.panic_mode = True


    # Exit a parse tree produced by ExprParser#term.
    def exitTerm(self, ctx:ExprParser.TermContext):
        pass


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

        
    def report_error(self, ctx, message):
        line = ctx.start.line if ctx.start else "unknown"
        print(f"Error en línea {line}: {message}")
        exit(1)
        
    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        pass  # Puedes imprimir un mensaje si lo deseas, pero dejarlo vacío evita el error.

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        pass  # Lo mismo aquí, si quieres registrar algo, usa print()
