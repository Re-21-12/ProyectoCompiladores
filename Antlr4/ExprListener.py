from antlr4 import *

if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# Esta clase define un completo listener para el árbol de análisis generado por ExprParser.
class ExprListener(ParseTreeListener):
    
    def __init__(self):
        # Inicializa la tabla de símbolos y las funciones declaradas
        self.symbol_table = {}
        self.functions = {}

    # Enter a parse tree produced by ExprParser#gramatica.
    def enterGramatica(self, ctx:ExprParser.GramaticaContext):
        pass

    # Exit a parse tree produced by ExprParser#gramatica.
    def exitGramatica(self, ctx:ExprParser.GramaticaContext):
        pass

    # Enter a parse tree produced by ExprParser#programa.
    def enterPrograma(self, ctx:ExprParser.ProgramaContext):
        pass

    # Exit a parse tree produced by ExprParser#programa.
    def exitPrograma(self, ctx:ExprParser.ProgramaContext):
        pass

    # Enter a parse tree produced by ExprParser#bloque.
    def enterBloque(self, ctx:ExprParser.BloqueContext):
        pass

    # Exit a parse tree produced by ExprParser#bloque.
    def exitBloque(self, ctx:ExprParser.BloqueContext):
        pass

    # Enter a parse tree produced by ExprParser#sentencia.
    def enterSentencia(self, ctx:ExprParser.SentenciaContext):
        pass

    # Exit a parse tree produced by ExprParser#sentencia.
    def exitSentencia(self, ctx:ExprParser.SentenciaContext):
        pass

    # Enter a parse tree produced by ExprParser#sentencia_if.
    def enterSentencia_if(self, ctx:ExprParser.Sentencia_ifContext):
        pass

    # Exit a parse tree produced by ExprParser#sentencia_if.
    def exitSentencia_if(self, ctx:ExprParser.Sentencia_ifContext):
        pass

    # Enter a parse tree produced by ExprParser#sentencia_while.
    def enterSentencia_while(self, ctx:ExprParser.Sentencia_whileContext):
        pass

    # Exit a parse tree produced by ExprParser#sentencia_while.
    def exitSentencia_while(self, ctx:ExprParser.Sentencia_whileContext):
        pass

    # Enter a parse tree produced by ExprParser#sentencia_for.
    def enterSentencia_for(self, ctx:ExprParser.Sentencia_forContext):
        pass

    # Exit a parse tree produced by ExprParser#sentencia_for.
    def exitSentencia_for(self, ctx:ExprParser.Sentencia_forContext):
        pass

    # Enter a parse tree produced by ExprParser#declaracion_funcion.
    def enterDeclaracion_funcion(self, ctx: ExprParser.Declaracion_funcionContext):
        nombre_funcion = ctx.VARIABLE().getText()
        parametros = [param.VARIABLE().getText() for param in ctx.parametros().parametro()]
        if nombre_funcion in self.functions:
            print(f"Error: Funcion '{nombre_funcion}' ya declarada.")
        else:
            self.functions[nombre_funcion] = parametros

    # Exit a parse tree produced by ExprParser#declaracion_funcion.
    def exitDeclaracion_funcion(self, ctx:ExprParser.Declaracion_funcionContext):
        pass

    # Enter a parse tree produced by ExprParser#funcion_llamada.
    def enterFuncion_llamada(self, ctx: ExprParser.Funcion_llamadaContext):
        nombre_funcion = ctx.VARIABLE().getText()
        argumentos = len(ctx.argumentos().expr())
        if nombre_funcion not in self.functions:
            print(f"Error: Funcion '{nombre_funcion}' no declarada.")
        else:
            parametros_funcion = len(self.functions[nombre_funcion])
            if argumentos != parametros_funcion:
                print(f"Error: Funcion '{nombre_funcion}' espera {parametros_funcion} argumentos, pero recibió {argumentos}.")

    # Exit a parse tree produced by ExprParser#funcion_llamada.
    def exitFuncion_llamada(self, ctx:ExprParser.Funcion_llamadaContext):
        pass

    # Enter a parse tree produced by ExprParser#declaracion.
    def enterDeclaracion(self, ctx: ExprParser.DeclaracionContext):
        tipo = ctx.tipo().getText()
        identificador = ctx.VARIABLE().getText()
        if identificador in self.symbol_table:
            print(f"Error: Variable '{identificador}' ya declarada.")
        else:
            self.symbol_table[identificador] = tipo

    # Exit a parse tree produced by ExprParser#declaracion.
    def exitDeclaracion(self, ctx:ExprParser.DeclaracionContext):
        pass

    # Enter a parse tree produced by ExprParser#reasignacion.
    def enterReasignacion(self, ctx: ExprParser.ReasignacionContext):
        identificador = ctx.VARIABLE().getText()
        if identificador not in self.symbol_table:
            print(f"Error: Variable '{identificador}' no declarada.")

    # Exit a parse tree produced by ExprParser#reasignacion.
    def exitReasignacion(self, ctx:ExprParser.ReasignacionContext):
        pass

    # Other enter/exit methods can go here (e.g., for expression, type, etc.)
    # Ejemplo de un chequeo de tipo básico en una asignación
    def check_type_assignment(self, variable, value):
        var_type = self.symbol_table.get(variable)
        if var_type != value:
            print(f"Error de tipo: la variable '{variable}' es de tipo '{var_type}', pero se intentó asignar un valor de tipo '{value}'.")
    # ! Posible inferencia de tipos
        # Ejemplo simple de inferencia de tipo
    def infer_type(self, expression):
        # Suponiendo que tienes algún tipo de lógica para deducir el tipo
        if isinstance(expression, int):
            return "int"
        elif isinstance(expression, float):
            return "float"
        else:
            return "unknown"
        
""" 
TODO: 
Falta inferencia de tipos
? Alterar gramatica (?)
"""
# TODO: Control de ambitos
# TODO: Manejo de errores (Modo panico, recuperacion a nivel de frases, errores logicos y semanticos)
