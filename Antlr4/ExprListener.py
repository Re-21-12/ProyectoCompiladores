# Generated from Expr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

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
    def enterDeclaracion_funcion(self, ctx:ExprParser.Declaracion_funcionContext):
        pass

    # Exit a parse tree produced by ExprParser#declaracion_funcion.
    def exitDeclaracion_funcion(self, ctx:ExprParser.Declaracion_funcionContext):
        pass


    # Enter a parse tree produced by ExprParser#funcion_llamada.
    def enterFuncion_llamada(self, ctx:ExprParser.Funcion_llamadaContext):
        pass

    # Exit a parse tree produced by ExprParser#funcion_llamada.
    def exitFuncion_llamada(self, ctx:ExprParser.Funcion_llamadaContext):
        pass


    # Enter a parse tree produced by ExprParser#funcion_llamada_expr.
    def enterFuncion_llamada_expr(self, ctx:ExprParser.Funcion_llamada_exprContext):
        pass

    # Exit a parse tree produced by ExprParser#funcion_llamada_expr.
    def exitFuncion_llamada_expr(self, ctx:ExprParser.Funcion_llamada_exprContext):
        pass


    # Enter a parse tree produced by ExprParser#retorna.
    def enterRetorna(self, ctx:ExprParser.RetornaContext):
        pass

    # Exit a parse tree produced by ExprParser#retorna.
    def exitRetorna(self, ctx:ExprParser.RetornaContext):
        pass


    # Enter a parse tree produced by ExprParser#parametros.
    def enterParametros(self, ctx:ExprParser.ParametrosContext):
        pass

    # Exit a parse tree produced by ExprParser#parametros.
    def exitParametros(self, ctx:ExprParser.ParametrosContext):
        pass


    # Enter a parse tree produced by ExprParser#parametro.
    def enterParametro(self, ctx:ExprParser.ParametroContext):
        pass

    # Exit a parse tree produced by ExprParser#parametro.
    def exitParametro(self, ctx:ExprParser.ParametroContext):
        pass


    # Enter a parse tree produced by ExprParser#argumentos.
    def enterArgumentos(self, ctx:ExprParser.ArgumentosContext):
        pass

    # Exit a parse tree produced by ExprParser#argumentos.
    def exitArgumentos(self, ctx:ExprParser.ArgumentosContext):
        pass


    # Enter a parse tree produced by ExprParser#bloque_condicional.
    def enterBloque_condicional(self, ctx:ExprParser.Bloque_condicionalContext):
        pass

    # Exit a parse tree produced by ExprParser#bloque_condicional.
    def exitBloque_condicional(self, ctx:ExprParser.Bloque_condicionalContext):
        pass


    # Enter a parse tree produced by ExprParser#bloque_de_sentencia.
    def enterBloque_de_sentencia(self, ctx:ExprParser.Bloque_de_sentenciaContext):
        pass

    # Exit a parse tree produced by ExprParser#bloque_de_sentencia.
    def exitBloque_de_sentencia(self, ctx:ExprParser.Bloque_de_sentenciaContext):
        pass


    # Enter a parse tree produced by ExprParser#declaracion.
    def enterDeclaracion(self, ctx:ExprParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by ExprParser#declaracion.
    def exitDeclaracion(self, ctx:ExprParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by ExprParser#declaracion_sin_asignacion.
    def enterDeclaracion_sin_asignacion(self, ctx:ExprParser.Declaracion_sin_asignacionContext):
        pass

    # Exit a parse tree produced by ExprParser#declaracion_sin_asignacion.
    def exitDeclaracion_sin_asignacion(self, ctx:ExprParser.Declaracion_sin_asignacionContext):
        pass


    # Enter a parse tree produced by ExprParser#reasignacion.
    def enterReasignacion(self, ctx:ExprParser.ReasignacionContext):
        pass

    # Exit a parse tree produced by ExprParser#reasignacion.
    def exitReasignacion(self, ctx:ExprParser.ReasignacionContext):
        pass


    # Enter a parse tree produced by ExprParser#tipo.
    def enterTipo(self, ctx:ExprParser.TipoContext):
        pass

    # Exit a parse tree produced by ExprParser#tipo.
    def exitTipo(self, ctx:ExprParser.TipoContext):
        pass


    # Enter a parse tree produced by ExprParser#mostrar.
    def enterMostrar(self, ctx:ExprParser.MostrarContext):
        pass

    # Exit a parse tree produced by ExprParser#mostrar.
    def exitMostrar(self, ctx:ExprParser.MostrarContext):
        pass


    # Enter a parse tree produced by ExprParser#expr.
    def enterExpr(self, ctx:ExprParser.ExprContext):
        pass

    # Exit a parse tree produced by ExprParser#expr.
    def exitExpr(self, ctx:ExprParser.ExprContext):
        pass


    # Enter a parse tree produced by ExprParser#term.
    def enterTerm(self, ctx:ExprParser.TermContext):
        pass

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
    def enterActualizacion(self, ctx:ExprParser.ActualizacionContext):
        pass

    # Exit a parse tree produced by ExprParser#actualizacion.
    def exitActualizacion(self, ctx:ExprParser.ActualizacionContext):
        pass


    # Enter a parse tree produced by ExprParser#sentencia_switch.
    def enterSentencia_switch(self, ctx:ExprParser.Sentencia_switchContext):
        pass

    # Exit a parse tree produced by ExprParser#sentencia_switch.
    def exitSentencia_switch(self, ctx:ExprParser.Sentencia_switchContext):
        pass



del ExprParser