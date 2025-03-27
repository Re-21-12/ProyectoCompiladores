from ExprParser import ExprParser
from visitors.ExprBaseVisitor import *
from visitors.ExprFunctionsVisitor import *

class ExprStatementVisitor(ExprBaseVisitor):

    def visitSentencia(self, ctx: ExprParser.SentenciaContext):
        if ctx.sentencia_if():
            return self.visitSentencia_if(ctx.sentencia_if())
        elif ctx.sentencia_while():
            return self.visitSentencia_while(ctx.sentencia_while())
        elif ctx.sentencia_for():
            return self.visitSentencia_for(ctx.sentencia_for())
        elif ctx.reasignacion():
            return self.visitReasignacion(ctx.reasignacion())
        elif ctx.declaracion():
            return self.visitDeclaracion(ctx.declaracion())
        elif ctx.mostrar():
            return self.visitMostrar(ctx.mostrar())
        elif ctx.declaracion_funcion():
            return self.visitDeclaracion_funcion(ctx.declaracion_funcion())
        elif ctx.funcion_llamada():
            return self.funcion_llamada(ctx.funcion_llamada())
        else:
            raise ValueError("Sentencia no reconocida")
        
    def visitDeclaracion_funcion(self, ctx:ExprParser.Declaracion_funcionContext):
        return ExprFunctionsVisitor().visitDeclaracion_funcion(self,ctx)

    # Visit a parse tree produced by ExprParser#funcion_llamada.
    def visitFuncion_llamada(self, ctx:ExprParser.Funcion_llamadaContext):
        return ExprFunctionsVisitor().visitFuncion_llamada(self,ctx)

    # Visit a parse tree produced by ExprParser#parametros.
    def visitParametros(self, ctx:ExprParser.ParametrosContext):
        return ExprFunctionsVisitor().visitParametros(self,ctx)

    # Visit a parse tree produced by ExprParser#parametro.
    def visitParametro(self, ctx:ExprParser.ParametroContext):
        return ExprFunctionsVisitor().visitParametro(self,ctx)

    # Visit a parse tree produced by ExprParser#argumentos.
    def visitArgumentos(self, ctx:ExprParser.ArgumentosContext):
        return ExprFunctionsVisitor().visitArgumentos(self,ctx)
    
    def visitSentencia_if(self, ctx: ExprParser.Sentencia_ifContext):
        bloques_condicionales = ctx.bloque_condicional()
        if isinstance(bloques_condicionales, list):
            condition_value = self.visit(bloques_condicionales[0].expr())
        else:
            condition_value = self.visit(bloques_condicionales.expr())

        if condition_value:
            self.visit(bloques_condicionales[0].bloque_de_sentencia())
            return
        else:
            for i in range(1, len(bloques_condicionales)):
                elif_condition = self.visit(bloques_condicionales[i].expr())
                if elif_condition:
                    self.visit(bloques_condicionales[i].bloque_de_sentencia())
                    return

            if ctx.ELSE():
                self.visit(ctx.bloque_de_sentencia())

    def visitSentencia_while(self, ctx: ExprParser.Sentencia_whileContext):
        while self.visit(ctx.bloque_condicional().expr()):
            self.visit(ctx.bloque_condicional().bloque_de_sentencia())

    def visitSentencia_for(self, ctx: ExprParser.Sentencia_forContext):
        self.visit(ctx.declaracion())
        while self.visit(ctx.expr()):
            self.visit(ctx.bloque_de_sentencia())
            self.visit(ctx.actualizacion())
