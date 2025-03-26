from antlr4 import ParseTreeVisitor

from ExprVisitor import ExprVisitor
from ExprParser import ExprParser
# visitors modularizados
from visitors.ExprMathVisitor import *
from visitors.ExprBaseVisitor import *
from visitors.ExprStatementVisitor import *
from visitors.ExprVariableVisitor import *

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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#sentencia.
    def visitSentencia(self, ctx: ExprParser.SentenciaContext):
        return ExprStatementVisitor.visitSentencia(self, ctx)

    def visitSentencia_if(self, ctx: ExprParser.Sentencia_ifContext):
        return ExprStatementVisitor.visitSentencia_if(self, ctx)
    # Visit a parse tree produced by ExprParser#sentencia_if.
    def visitBloque_de_sentencia(self, ctx: ExprParser.Bloque_de_sentenciaContext):
        if ctx.sentencia():
            for sentencia in ctx.sentencia():
                self.visit(sentencia)
        elif ctx.getChildCount() == 1:
            self.visit(ctx.getChild(0))


    # Visit a parse tree produced by ExprParser#sentencia_while.
    def visitSentencia_while(self, ctx: ExprParser.Sentencia_whileContext):
        ExprStatementVisitor.visitSentencia_while(self, ctx)
             
            


    # Visit a parse tree produced by ExprParser#sentencia_for.
    def visitSentencia_for(self, ctx: ExprParser.Sentencia_forContext):
        ExprStatementVisitor.visitSentencia_for(self, ctx)


    # Visit a parse tree produced by ExprParser#bloque_condicional.
    def visitBloque_condicional(self, ctx:ExprParser.Bloque_condicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#bloque_de_sentencia.
    def visitBloque_de_sentencia(self, ctx:ExprParser.Bloque_de_sentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#declaracion.
    def visitDeclaracion(self, ctx: ExprParser.DeclaracionContext):
       return ExprVariableVisitor.visitDeclaracion(self, ctx)


    # Visit a parse tree produced by ExprParser#reasignacion.
    def visitReasignacion(self, ctx: ExprParser.ReasignacionContext):
        ExprVariableVisitor.visitReasignacion(self, ctx)


    # Visit a parse tree produced by ExprParser#tipo.
    def visitTipo(self, ctx:ExprParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#mostrar.
    def visitMostrar(self, ctx:ExprParser.MostrarContext):
        value = self.visit(ctx.expr())
        print(value)

    # Visit a parse tree produced by ExprParser#expr.
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
            if left is None or right is None:
                raise ValueError("No se puede comparar None con un número")
            result = left < right
        elif operator.getText() == '>':
            if left is None or right is None:
                raise ValueError("No se puede comparar None con un número")
            result = left > right
        elif operator.getText() == '<=':
            if left is None or right is None:
                raise ValueError("No se puede comparar None con un número")
            result = left <= right
        elif operator.getText() == '>=':
            if left is None or right is None:
                raise ValueError("No se puede comparar None con un número")
            result = left >= right
        elif operator.getText() == '==':
            if left is None or right is None:
                raise ValueError("No se puede comparar None con un número")
            result = left == right
        elif operator.getText() == '!=':
            if left is None or right is None:
                raise ValueError("No se puede comparar None con un número")
            result = left != right
        else:
            raise ValueError(f"Operador desconocido {operator.getText()}")
 
        print(f"Resultado de la evaluación: {result}")
        return result

    # Visit a parse tree produced by ExprParser#term.
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
 

        # Visit a parse tree produced by ExprParser#factor.
    def visitFactor(self, ctx: ExprParser.FactorContext):
        if ctx.NUMERO():
            return int(ctx.NUMERO().getText())
        elif ctx.DECIMAL():
            return float(ctx.DECIMAL().getText())
        elif ctx.BOOLEANO():
            return ctx.BOOLEANO().getText() == "verdadero"  # Devuelve True si es 'true', False si es 'false'
        elif ctx.CADENA():
            return ctx.CADENA().getText()[1:-1]  # Elimina las comillas de la cadena
        elif ctx.VARIABLE():
            var_name = ctx.VARIABLE().getText()
            if var_name in self.variables:
                return self.variables[var_name]
            else:
                raise NameError(f"Variable no definida: {var_name}")
        elif ctx.PARENTESIS_INICIAL():
            return self.visit(ctx.getChild(1))
        elif ctx.MENOS():
            return -self.visit(ctx.getChild(1))
        elif ctx.VARIABLE() and ctx.MASMAS():
            var_name = ctx.VARIABLE().getText()
            self.variables[var_name] = self.variables.get(var_name, 0) + 1
            return self.variables[var_name]
        elif ctx.VARIABLE() and ctx.MENOSMENOS():
            var_name = ctx.VARIABLE().getText()
            self.variables[var_name] = self.variables.get(var_name, 0) - 1
            return self.variables[var_name]
        else:
            raise ValueError("Operación no soportada")

 

    # Visit a parse tree produced by ExprParser#actualizacion.
    def visitActualizacion(self, ctx: ExprParser.ActualizacionContext):
        ExprVariableVisitor.visitActualizacion(self, ctx)



del ExprParser