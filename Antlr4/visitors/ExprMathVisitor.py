from ExprParser import ExprParser
from visitors.ExprBaseVisitor import *

class ExprMathVisitor(ExprBaseVisitor):

    def visitExpr(self, ctx: ExprParser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))

        left = self.visit(ctx.getChild(0))
        operator = ctx.getChild(1).getText()
        right = self.visit(ctx.getChild(2))

        if isinstance(left, str) or isinstance(right, str):
            if operator == '+':
                return str(left) + str(right)
            else:
                raise TypeError(f"Operación no válida entre cadenas: {left} {operator} {right}")

        if isinstance(left, bool) or isinstance(right, bool):
            raise TypeError(f"Operación no válida entre booleanos: {left} {operator} {right}")
        
        if isinstance(left, (int, float)) and isinstance(right, (int, float)):
            if operator == '+':
                return left + right
            elif operator == '-':
                return left - right
            elif operator == '<':
                return left < right
            elif operator == '>':
                return left > right
            elif operator == '<=':
                return left <= right
            elif operator == '>=':
                return left >= right
            elif operator == '==':
                return left == right
            elif operator == '!=':
                return left != right
            else:
                raise ValueError(f"Operador desconocido {operator}")
        
        raise TypeError(f"Tipos incompatibles: {type(left)} {operator} {type(right)}")

    def visitTerm(self, ctx: ExprParser.TermContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))

        left = self.visit(ctx.getChild(0))
        operator = ctx.getChild(1).getText()
        right = self.visit(ctx.getChild(2))

        if not isinstance(left, (int, float)) or not isinstance(right, (int, float)):
            raise TypeError(f"Operación no válida entre tipos: {type(left)} {operator} {type(right)}")

        if operator == '*':
            return left * right
        elif operator == '/':
            if right == 0:
                raise ZeroDivisionError("División por cero no permitida")
            return left / right
        else:
            raise ValueError(f"Operador desconocido {operator}")

    def visitFactor(self, ctx: ExprParser.FactorContext):
        if ctx.NUMERO():
            return int(ctx.NUMERO().getText())
        elif ctx.DECIMAL():
            return float(ctx.DECIMAL().getText())
        elif ctx.BOOLEANO():
            return ctx.BOOLEANO().getText() == 'verdadero'
        elif ctx.CADENA():
            return ctx.CADENA().getText().strip('"')
        elif ctx.VARIABLE():
            var_name = ctx.VARIABLE().getText()
            try:
                return self.get_variable(var_name)  # Se busca la variable en los ámbitos
            except NameError:
                raise NameError(f"Variable no definida [FACTOR]: {var_name}")
        else:
            raise ValueError("Expresión no válida")
