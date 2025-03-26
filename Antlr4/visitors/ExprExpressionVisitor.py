from ExprParser import ExprParser


from visitors.ExprBaseVisitor import *

class ExprExpressionVisitor(ExprBaseVisitor):
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
