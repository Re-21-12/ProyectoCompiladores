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
        pass

    # Exit a parse tree produced by ExprParser#sentencia_for.
    def exitSentencia_for(self, ctx: ExprParser.Sentencia_forContext):
        pass

    # Al entrar a una función, creamos un nuevo ámbito
    def enterDeclaracion_funcion(self, ctx: ExprParser.Declaracion_funcionContext):
        self.symbol_table.enter_scope()

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
        pass

    # Exit a parse tree produced by ExprParser#bloque_condicional.
    def exitBloque_condicional(self, ctx: ExprParser.Bloque_condicionalContext):
        pass

    # Enter a parse tree produced by ExprParser#bloque_de_sentencia.
    def enterBloque_de_sentencia(self, ctx: ExprParser.Bloque_de_sentenciaContext):
        pass

    # Exit a parse tree produced by ExprParser#bloque_de_sentencia.
    def exitBloque_de_sentencia(self, ctx: ExprParser.Bloque_de_sentenciaContext):
        pass

    # Enter a parse tree produced by ExprParser#declaracion.
    def enterDeclaracion(self, ctx: ExprParser.DeclaracionContext):
        var_name = ctx.VARIABLE().getText()  # Obtén el nombre de la variable
        var_type = ctx.tipo().getText()  # Obtén el tipo de la variable
        value = self.visit(ctx.expr())
        
        if var_type == "entero":
            if not isinstance(value, int):
                raise TypeError(f"Error de tipo: Se esperaba un valor de tipo 'entero' para la variable '{var_name}', pero se obtuvo {self.traducir_tipo(value)}")
        elif var_type == "decimal":
            if not isinstance(value, float):
                raise TypeError(f"Error de tipo: Se esperaba un valor de tipo 'decimal' para la variable '{var_name}', pero se obtuvo {self.traducir_tipo(value)}")
        elif var_type == "cadena":
            if not isinstance(value, str):
                raise TypeError(f"Error de tipo: Se esperaba un valor de tipo 'cadena' para la variable '{var_name}', pero se obtuvo {self.traducir_tipo(value)}")
        elif var_type == "bool":
            if not isinstance(value, bool):
                raise TypeError(f"Error de tipo: Se esperaba un valor de tipo 'bool' para la variable '{var_name}', pero se obtuvo {self.traducir_tipo(value)}")
            
        try:
            self.symbol_table.declare_variable(var_name, var_type)
        except ValueError as e:
            print(f"Error: {e}")
            self.panic_mode = True  # Activar el modo pánico en caso de error

    # Exit a parse tree produced by ExprParser#declaracion.
    def exitDeclaracion(self, ctx: ExprParser.DeclaracionContext):
        pass

    # Cuando entras a una asignación
    def enterReasignacion(self, ctx: ExprParser.ReasignacionContext):
        var_name = ctx.VARIABLE().getText()
        var_type = self.symbol_table.get_variable(var_name)
        
        if var_type is None:
            print(f"Error: La variable '{var_name}' no ha sido declarada.")
            self.panic_mode = True  # Activar el modo pánico en caso de error
        else:
            assigned_type = self.get_expression_type(ctx.expr())
            if assigned_type != var_type:
                print(f"Error: Asignación de tipo incompatible a '{var_name}'. Esperado: {var_type}, Encontrado: {assigned_type}")
                self.panic_mode = True  # Activar el modo pánico en caso de error

    # Exit a parse tree produced by ExprParser#reasignacion.
    def exitReasignacion(self, ctx: ExprParser.ReasignacionContext):
        pass

    def enterExpr(self, ctx: ExprParser.ExprContext):
        if ctx.getChildCount() == 3:  # Expresión binaria (ej: a + b)
            left = ctx.getChild(0)
            operator = ctx.getChild(1).getText()
            right = ctx.getChild(2)

            left_name = left.getText()
            right_name = right.getText()

            left_type = self.symbol_table.get_variable_type(left_name)
            right_type = self.symbol_table.get_variable_type(right_name)

            if left_type is None or right_type is None:
                print(f"Error: Variable no declarada en la expresión '{left_name} {operator} {right_name}'")
                self.panic_mode = True
                return

            # Reglas de validación de tipos
            if operator in {'+', '-', '*', '/'}:
                if left_type in {'entero', 'decimal'} and right_type in {'entero', 'decimal'}:
                    pass  # Operación válida
                elif operator == '+' and left_type == 'cadena' and right_type == 'cadena':
                    pass  # Concatenación de cadenas es válida
                else:
                    print(f"Error: No se puede aplicar '{operator}' entre '{left_type}' y '{right_type}'")
                    self.panic_mode = True

            elif operator in {'==', '!=', '<', '>', '<=', '>='}:
                if left_type == right_type:  # Comparación válida si ambos operandos son del mismo tipo
                    pass
                else:
                    print(f"Error: Comparación inválida entre '{left_type}' y '{right_type}'")
                    self.panic_mode = True

    # Exit a parse tree produced by ExprParser#expr.
    def exitExpr(self, ctx: ExprParser.ExprContext):
        pass

    # Método auxiliar para determinar el tipo de una expresión
    def get_expression_type(self, expr_ctx:ExprParser.ExprContext):
        # Este es un método simple para obtener el tipo de una expresión, debería ser extendido para manejar más casos.
        if isinstance(expr_ctx, ExprParser.NUMERO):
            return 'int'
        if isinstance(expr_ctx, ExprParser.DECIMAL):
            return 'decimal'
        elif isinstance(expr_ctx, ExprParser.CADENA):
            return 'string'
        elif isinstance(expr_ctx, ExprParser.BOOLEANO):
            return 'bool'
        # Aquí puedes agregar más lógica para determinar el tipo basado en el contexto de la expresión
        return 'unknown'

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

    def traducir_tipo(tipo):
        if isinstance(tipo, int):
            return "entero"
        elif isinstance(tipo, float):
            return "decimal"
        elif isinstance(tipo, str):
            return "cadena"
        elif isinstance(tipo, bool):
            return "bool"
        else:
            raise ValueError(f"El tipo de dato no es el correcto: {tipo}")