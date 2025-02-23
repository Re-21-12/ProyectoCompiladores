# Generated from Expr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):
 
    def __init__(self):
        self.variables = {}  # Almacena las variables y sus valores
 
    # Visit a parse tree produced by ExprParser#gramatica.
    def visitGramatica(self, ctx:ExprParser.GramaticaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#programa.
    def visitPrograma(self, ctx:ExprParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#bloque.
    def visitBloque(self, ctx:ExprParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#bloque_condicional.
    def visitBloque_condicional(self, ctx:ExprParser.Bloque_condicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#bloque_de_sentencia.
    def visitBloque_de_sentencia(self, ctx:ExprParser.Bloque_de_sentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#bloque_for.
    def visitBloque_for(self, ctx: ExprParser.Bloque_forContext):
        # Inicialización
        init_expr = self.visit(ctx.expr(0))  # Expresión inicial
        # Condición
        condition_expr = self.visit(ctx.expr(1))  # Expresión de la condición
        # Actualización
        update_expr = self.visit(ctx.expr(2))  # Expresión de actualización
        
        # Ejecutar el ciclo while la condición sea verdadera
        while condition_expr:
            # Ejecutar el bloque dentro del for
            self.visit(ctx.bloque())  # Visitar el bloque de código dentro del for
            
            # Actualizar la variable de control del for
            update_expr = self.visit(ctx.expr(2))  # Evaluar la expresión de actualización
            
            # Volver a evaluar la condición
            condition_expr = self.visit(ctx.expr(1))  # Evaluar la condición nuevamente

        return None  # El bloque for no devuelve un valor directamente

       # Visit a parse tree produced by ExprParser#declaracion.
    def visitDeclaracion(self, ctx: ExprParser.DeclaracionContext):
        var_name = ctx.VARIABLE().getText()  # Obtener el nombre de la variable
        value = self.visit(ctx.getChild(2))  # Obtener el valor de la expresión (a la derecha del '=')
        self.variables[var_name] = value  # Asignar el valor a la variable
        print(f" Variable: {value}")
 
        return value  # Retornar el valor de la asignación

    # Visit a parse tree produced by ExprParser#sentencia.
    def visitSentencia(self, ctx:ExprParser.SentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#sentencia_if.
    def visitSentencia_if(self, ctx: ExprParser.Sentencia_ifContext):
        # Visitar la condición (bloque_condicional)
        condition_value = self.visit(ctx.bloque_condicional().expr())
        if condition_value:
            # Si la condición es verdadera, visitar el bloque dentro del if
            self.visit(ctx.bloque_condicional().bloque_de_sentencia())
        else:
            # Si hay un bloque ELSE, se evalúa
            if ctx.ELSE():
                self.visit(ctx.bloque_de_sentencia())  # Visitar el bloque del else
            # Si hay else ifs, recorrerlos
            for elif_block in ctx.ELSEIF():
                elif_condition = self.visit(elif_block.bloque_condicional().expr())
                if elif_condition:
                    self.visit(elif_block.bloque_condicional().bloque_de_sentencia())
                    break  # Si se ejecutó un bloque, no seguimos evaluando más condiciones


    # Visit a parse tree produced by ExprParser#sentencia_while.
    def visitSentencia_while(self, ctx: ExprParser.Sentencia_whileContext):
    # Evaluar la condición del while
        while self.visit(ctx.expr()):
            self.visit(ctx.bloque_de_sentencia())  # Ejecutar el bloque de sentencia mientras la condición sea verdadera


    # Visit a parse tree produced by ExprParser#sentencia_for.
    def visitSentencia_for(self, ctx: ExprParser.Sentencia_forContext):
    # Primero ejecutamos la declaración (asignación)
        self.visit(ctx.declaracion())
    
    # Condición del ciclo
        while self.visit(ctx.expr()):
        # Ejecutamos el bloque dentro del for
            self.visit(ctx.bloque_de_sentencia())
            # Realizamos el incremento/decremento de la variable en el ciclo
            self.visit(ctx.getChild(4))  # El último hijo es la parte de actualización del ciclo


    # Visit a parse tree produced by ExprParser#expr.
    def visitExpr(self, ctx: ExprParser.ExprContext):
        if ctx.getChildCount() == 1:  # Caso base: un solo término
            return self.visit(ctx.getChild(0))  # Visitar el primer hijo (que será un factor)

        left = self.visit(ctx.getChild(0))  # El primer término
        operator = ctx.getChild(1)  # El operador (MAS, MENOS, o lógico)
        right = self.visit(ctx.getChild(2))  # El segundo término

        print(f"Variable L E: {left}")
        print(f"Variable R E: {right}")

        # Aritméticos
        if operator.getText() == '+':
            result = left + right
        elif operator.getText() == '-':
            result = left - right
        # Operadores de comparación
        elif operator.getText() == '<':
            result = left < right
        elif operator.getText() == '>':
            result = left > right
        elif operator.getText() == '<=':
            result = left <= right
        elif operator.getText() == '>=':
            result = left >= right
        else:
            raise ValueError(f"Operador desconocido {operator.getText()}")

        print(f"Resultado de la evaluación: {result}")

        return result  # Retornar el resultado de la operación

      # Visit a parse tree produced by ExprParser#term.
    def visitTerm(self, ctx: ExprParser.TermContext):
        if ctx.getChildCount() == 1:  # Caso base: un solo factor
            return self.visit(ctx.getChild(0))  # Visitar el primer hijo (que será un factor)
 
        left = self.visit(ctx.getChild(0))  # El primer factor
        operator = ctx.getChild(1)  # El operador (MULTIPLICACION o DIVISION)
        right = self.visit(ctx.getChild(2))  # El segundo factor
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
        if ctx.NUMERO():  # Si es un número
            return int(ctx.NUMERO().getText())  # Convertir el texto del número a entero
        elif ctx.DECIMAL():  # Si es un número decimal
            return float(ctx.DECIMAL().getText())  # Convertir el texto del número decimal
        elif ctx.VARIABLE():  # Si es una variable
            var_name = ctx.VARIABLE().getText()
            if var_name in self.variables:
                return self.variables[var_name]  # Devolver el valor almacenado de la variable
            else:
                raise NameError(f"Variable no definida: {var_name}")
        elif ctx.PARENTESIS_INICIAL():  # Si está entre paréntesis
            return self.visit(ctx.getChild(1))  # Visitar el contenido dentro de los paréntesis
        elif ctx.MENOS():  # Si es un número negativo
            return -self.visit(ctx.getChild(1))  # Negar el valor del factor siguiente
        elif ctx.VARIABLE() and ctx.MASMAS():  # Si es un incremento unario
            var_name = ctx.VARIABLE().getText()
            self.variables[var_name] = self.variables.get(var_name, 0) + 1
            return self.variables[var_name]
        elif ctx.VARIABLE() and ctx.MENOSMENOS():  # Si es un decremento unario
            var_name = ctx.VARIABLE().getText()
            self.variables[var_name] = self.variables.get(var_name, 0) - 1
            return self.variables[var_name]
        else:
            raise ValueError("Operación no soportada")
 

del ExprParser