import SymbolTable
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener, SymbolTable):
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

    # Validar que las variables usadas estén declaradas
    def enterExpr(self, ctx: ExprParser.ExprContext):
        if isinstance(ctx, ExprParser.VariableContext):
            var_name = ctx.VARIABLE().getText()
            if self.symbol_table.get_variable(var_name) is None:
                print(f"Error: La variable '{var_name}' utilizada sin declarar.")
                self.panic_mode = True  # Activar el modo pánico en caso de error

    # Exit a parse tree produced by ExprParser#expr.
    def exitExpr(self, ctx: ExprParser.ExprContext):
        pass

    # Método auxiliar para determinar el tipo de una expresión
    def get_expression_type(self, expr_ctx):
        # Este es un método simple para obtener el tipo de una expresión, debería ser extendido para manejar más casos.
        if isinstance(expr_ctx, ExprParser.NumeroContext):
            return 'int'
        elif isinstance(expr_ctx, ExprParser.CadenaContext):
            return 'string'
        elif isinstance(expr_ctx, ExprParser.BooleanoContext):
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
