# Generated from Expr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

def traducir_tipo(tipo):
    if  type(tipo) == int:
        return "entero"
    elif type(tipo) == float:
        return "decimal"
    else:
        raise ValueError(f"El tipo de dato no es el correcto: {tipo}")
    

class ExprVisitor(ParseTreeVisitor):

    def __init__(self):
        self.variables = {}

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
        elif ctx.actualizacion():
            return self.visitActualizacion(ctx.actualizacion())
        else:
            raise ValueError("Sentencia no reconocida")

    def visitSentencia_if(self, ctx: ExprParser.Sentencia_ifContext):
        bloques_condicionales = ctx.bloque_condicional()
        if isinstance(bloques_condicionales, list):
            condition_value = self.visit(bloques_condicionales[0].expr())
        else:
            condition_value = self.visit(bloques_condicionales.expr())

        print(f"Condición IF: {condition_value}")
        if condition_value:
            print("Ejecutando bloque IF")
            self.visit(bloques_condicionales[0].bloque_de_sentencia())
            return
        else:
            for i in range(1, len(bloques_condicionales)):
                elif_condition = self.visit(bloques_condicionales[i].expr())
                print(f"Condición ELSE IF {i}: {elif_condition}")
                if elif_condition:
                    print(f"Ejecutando bloque ELSE IF {i}")
                    self.visit(bloques_condicionales[i].bloque_de_sentencia())
                    return

            if ctx.ELSE():
                print("Ejecutando bloque ELSE")
                self.visit(ctx.bloque_de_sentencia())

    # Visit a parse tree produced by ExprParser#sentencia_if.
    def visitBloque_de_sentencia(self, ctx: ExprParser.Bloque_de_sentenciaContext):
        if ctx.sentencia():
            for sentencia in ctx.sentencia():
                self.visit(sentencia)
        elif ctx.getChildCount() == 1:
            self.visit(ctx.getChild(0))


    # Visit a parse tree produced by ExprParser#sentencia_while.
    def visitSentencia_while(self, ctx: ExprParser.Sentencia_whileContext):
        while self.visit(ctx.bloque_condicional().expr()):
            self.visit(ctx.bloque_condicional().bloque_de_sentencia())
             
            


    # Visit a parse tree produced by ExprParser#sentencia_for.
    def visitSentencia_for(self, ctx: ExprParser.Sentencia_forContext):
        self.visit(ctx.declaracion())
        while self.visit(ctx.expr()):
            self.visit(ctx.bloque_de_sentencia())
            self.visit(ctx.actualizacion())


    # Visit a parse tree produced by ExprParser#bloque_condicional.
    def visitBloque_condicional(self, ctx:ExprParser.Bloque_condicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#bloque_de_sentencia.
    def visitBloque_de_sentencia(self, ctx:ExprParser.Bloque_de_sentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#declaracion.
    def visitDeclaracion(self, ctx: ExprParser.DeclaracionContext):
        var_name = ctx.VARIABLE().getText()
        var_type = ctx.tipo().getText()
        value = self.visit(ctx.expr())
 
        if var_type == "entero":
            if not isinstance(value, int):
                raise TypeError(f"Error de tipo: Se esperaba un valor de tipo 'int' para la variable '{var_name}', pero se obtuvo {traducir_tipo(type(value))}")
        elif var_type == "decimal":
            if not isinstance(value, float):
                raise TypeError(f"Error de tipo: Se esperaba un valor de tipo 'float' para la variable '{var_name}', pero se obtuvo {traducir_tipo(type(value))}")
        else:
            raise TypeError(f"Tipo de variable no soportado: {var_type}")
 
        self.variables[var_name] = value
        return value


    # Visit a parse tree produced by ExprParser#reasignacion.
    def visitReasignacion(self, ctx: ExprParser.ReasignacionContext):
        var_name = ctx.VARIABLE().getText()
        new_value = self.visit(ctx.expr())
 
        if var_name in self.variables:
            original_value = self.variables[var_name]
 
            if isinstance(original_value, int) and not isinstance(new_value, int):
                raise TypeError(f"Error de tipo: La variable '{var_name}' es de tipo 'int', pero se intentó asignar un valor de tipo {traducir_tipo(type(new_value))}")
            elif isinstance(original_value, float) and not isinstance(new_value, float):
                raise TypeError(f"Error de tipo: La variable '{var_name}' es de tipo 'float', pero se intentó asignar un valor de tipo {traducir_tipo(type(new_value))}")
            else:
                print(f"Reasignando {var_name} a {new_value}")
                self.variables[var_name] = new_value
        else:
            raise NameError(f"Variable no definida: {var_name}")
 
        return new_value


    # Visit a parse tree produced by ExprParser#tipo.
    def visitTipo(self, ctx:ExprParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#mostrar.
    def visitMostrar(self, ctx:ExprParser.MostrarContext):
        value = self.visit(ctx.expr())
        print("mostrando" , value)

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
        var_name = ctx.VARIABLE().getText()
        print(f"Actualizando variable: {var_name}")
 
        if var_name not in self.variables:
            raise NameError(f"Variable no definida: {var_name}")
 
        if ctx.MASMAS():
            print(f"Incrementando {var_name}")
            self.variables[var_name] += 1
        elif ctx.MENOSMENOS():
            print(f"Decrementando {var_name}")
            self.variables[var_name] -= 1
        elif ctx.expr():
            new_value = self.visit(ctx.expr())
            self.variables[var_name] = new_value
 
        print(f"Nuevo valor de {var_name}: {self.variables[var_name]}")
        return self.variables[var_name]



del ExprParser