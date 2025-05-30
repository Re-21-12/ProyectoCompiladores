# Generated from Expr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#gramatica.
    def visitGramatica(self, ctx:ExprParser.GramaticaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#programa.
    def visitPrograma(self, ctx:ExprParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#bloque.
    def visitBloque(self, ctx:ExprParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#sentencia.
    def visitSentencia(self, ctx:ExprParser.SentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#sentencia_if.
    def visitSentencia_if(self, ctx:ExprParser.Sentencia_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#sentencia_while.
    def visitSentencia_while(self, ctx:ExprParser.Sentencia_whileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#sentencia_for.
    def visitSentencia_for(self, ctx:ExprParser.Sentencia_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#declaracion_funcion.
    def visitDeclaracion_funcion(self, ctx:ExprParser.Declaracion_funcionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#funcion_llamada.
    def visitFuncion_llamada(self, ctx:ExprParser.Funcion_llamadaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#funcion_llamada_expr.
    def visitFuncion_llamada_expr(self, ctx:ExprParser.Funcion_llamada_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#retorna.
    def visitRetorna(self, ctx:ExprParser.RetornaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#parametros.
    def visitParametros(self, ctx:ExprParser.ParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#parametro.
    def visitParametro(self, ctx:ExprParser.ParametroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#argumentos.
    def visitArgumentos(self, ctx:ExprParser.ArgumentosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#bloque_condicional.
    def visitBloque_condicional(self, ctx:ExprParser.Bloque_condicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#bloque_de_sentencia.
    def visitBloque_de_sentencia(self, ctx:ExprParser.Bloque_de_sentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#declaracion.
    def visitDeclaracion(self, ctx:ExprParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#declaracion_sin_asignacion.
    def visitDeclaracion_sin_asignacion(self, ctx:ExprParser.Declaracion_sin_asignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#reasignacion.
    def visitReasignacion(self, ctx:ExprParser.ReasignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#tipo.
    def visitTipo(self, ctx:ExprParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#mostrar.
    def visitMostrar(self, ctx:ExprParser.MostrarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#expr.
    def visitExpr(self, ctx:ExprParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#term.
    def visitTerm(self, ctx:ExprParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#factor.
    def visitFactor(self, ctx:ExprParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#actualizacion.
    def visitActualizacion(self, ctx:ExprParser.ActualizacionContext):
        return self.visitChildren(ctx)



del ExprParser