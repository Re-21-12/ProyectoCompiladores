from ExprParser import ExprParser
from ExprBaseVisitor import ExprBaseVisitor


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
        else:
            raise ValueError("Sentencia no reconocida")

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
