from antlr4 import ParseTreeVisitor
from ExprVisitor import ExprVisitor
from ExprParser import ExprParser
# Visitors modularizados
from visitors.ExprMathVisitor import *
from visitors.ExprBaseVisitor import *
from visitors.ExprStatementVisitor import *
from visitors.ExprVariableVisitor import *
from visitors.ExprFunctionsVisitor import *

def traducir_tipo(tipo):
    return ExprBaseVisitor.traducir_tipo(tipo)


class PersonalizatedVisitor(ParseTreeVisitor):
    def __init__(self):
        ExprBaseVisitor.__init__(self)


    # Visit a parse tree produced by ExprParser#gramatica.
    def visitGramatica(self, ctx:ExprParser.GramaticaContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#programa.
    def visitPrograma(self, ctx: ExprParser.ProgramaContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#bloque.
    def visitBloque(self, ctx:ExprParser.BloqueContext):
        ExprBaseVisitor.enter_scope(self)  # Inicia un nuevo ámbito local
        result = self.visitChildren(ctx)
        ExprBaseVisitor.exit_scope(self)   # Finaliza el ámbito local
        return result

    # Visit a parse tree produced by ExprParser#sentencia.
    def visitSentencia(self, ctx: ExprParser.SentenciaContext):
        return ExprStatementVisitor.visitSentencia(self, ctx)

    def visitDeclaracion_funcion(self, ctx:ExprParser.Declaracion_funcionContext):
        return ExprFunctionsVisitor.visitDeclaracion_funcion(self, ctx)

    # Visit a parse tree produced by ExprParser#funcion_llamada.
    def visitFuncion_llamada(self, ctx:ExprParser.Funcion_llamadaContext):
        return ExprFunctionsVisitor.visitFuncion_llamada(self,ctx)

    # Visit a parse tree produced by ExprParser#parametros.
    def visitParametros(self, ctx:ExprParser.ParametrosContext):
        return ExprFunctionsVisitor.visitParametros(self, ctx)

    # Visit a parse tree produced by ExprParser#parametro.
    def visitParametro(self, ctx:ExprParser.ParametroContext):
        return ExprFunctionsVisitor.visitParametro(self, ctx)

    # Visit a parse tree produced by ExprParser#argumentos.
    def visitArgumentos(self, ctx:ExprParser.ArgumentosContext):
        return ExprFunctionsVisitor.visitArgumentos(self, ctx)

    def visitSentencia_if(self, ctx: ExprParser.Sentencia_ifContext):
        return ExprStatementVisitor.visitSentencia_if(self, ctx)

    def visitBloque_de_sentencia(self, ctx: ExprParser.Bloque_de_sentenciaContext):
        if ctx.sentencia():
            for sentencia in ctx.sentencia():
                self.visit(sentencia)
        elif ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))  # Agregamos return aquí
        return None  # Retornamos None explícitamente

    def visitSentencia_while(self, ctx: ExprParser.Sentencia_whileContext):
        return ExprStatementVisitor.visitSentencia_while(self, ctx)

    def visitSentencia_for(self, ctx: ExprParser.Sentencia_forContext):
        return ExprStatementVisitor.visitSentencia_for(self, ctx)

    def visitBloque_condicional(self, ctx:ExprParser.Bloque_condicionalContext):
        return self.visitChildren(ctx)

    def visitDeclaracion(self, ctx: ExprParser.DeclaracionContext):
        var_name = ctx.VARIABLE().getText()
        value = self.visit(ctx.expr())  # Obtener el valor de la expresión
        ExprBaseVisitor.define_variable(self, var_name, value)

    def visitReasignacion(self, ctx: ExprParser.ReasignacionContext):
        var_name = ctx.VARIABLE().getText()
        value = self.visit(ctx.expr())  # Obtener el valor de la expresión
        ExprBaseVisitor.define_variable(self, var_name, value)

    def visitMostrar(self, ctx: ExprParser.MostrarContext):
        value = self.visit(ctx.expr())
        print(value)

    def visitExpr(self, ctx: ExprParser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))

        left = self.visit(ctx.getChild(0))
        operator = ctx.getChild(1)
        right = self.visit(ctx.getChild(2))

        print(f"Variable L E: {left}")
        print(f"Variable R E: {right}")
        print(f"Operador R E: {operator.getText()}")

        if operator.getText() == '+':
            result = left + right
        elif operator.getText() == '-':
            result = left - right
        elif operator.getText() == '<':
            result = left < right
        elif operator.getText() == '>':
            result = left > right
        elif operator.getText() == '<=':
            result = left <= right
        elif operator.getText() == '>=':
            result = left >= right
        elif operator.getText() == '==':
            result = left == right
        elif operator.getText() == '!=':
            result = left != right
        else:
            raise ValueError(f"Operador desconocido {operator.getText()}")

        print(f"Resultado de la evaluación: {result}")
        return result

    def visitTerm(self, ctx: ExprParser.TermContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))

        left = self.visit(ctx.getChild(0))
        operator = ctx.getChild(1)
        right = self.visit(ctx.getChild(2))

        print(f" Variable L T: {left}")
        print(f" Variable R T: {right}")
        if operator.getText() == '*':
            return left * right
        elif operator.getText() == '/':
            if right == 0:
                raise ZeroDivisionError("División por cero no permitida")
            return left / right
        else:
            raise ValueError(f"Operador desconocido {operator.getText()}")

    def visitFactor(self, ctx: ExprParser.FactorContext):
        if ctx.NUMERO():
            return int(ctx.NUMERO().getText())
        elif ctx.DECIMAL():
            return float(ctx.DECIMAL().getText())
        elif ctx.BOOLEANO():
            return ctx.BOOLEANO().getText() == "verdadero"
        elif ctx.CADENA():
            return ctx.CADENA().getText()[1:-1]  # Elimina las comillas
        elif ctx.VARIABLE():
            var_name = ctx.VARIABLE().getText()
            return ExprBaseVisitor.get_variable(self,var_name)
        elif ctx.PARENTESIS_INICIAL():
            return self.visit(ctx.getChild(1))
        elif ctx.MENOS():
            return -self.visit(ctx.getChild(1))
        else:
            raise ValueError("Operación no soportada")
