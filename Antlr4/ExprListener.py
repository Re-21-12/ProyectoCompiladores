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



del ExprParser