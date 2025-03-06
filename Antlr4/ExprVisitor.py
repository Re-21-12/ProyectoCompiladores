# Generated from Expr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

# funciones auxiliares
    def traducir_tipo(tipo):
        if  type(tipo) == int:
            return "entero"
        elif type(tipo) == float:
            return "decimal"
        else:
            raise ValueError(f"Tipo de dato no soportado: {tipo}")

class ExprVisitor(ParseTreeVisitor):

  
    def __init__(self):
        self.variables = {}  # Almacena las variables y sus valores
 
     # Visit a parse tree produced by ExprParser#mostrar.
    def visitMostrar(self, ctx:ExprParser.MostrarContext):
        value = self.visit(ctx.expr())
        print(value)
 
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
        self.visit(ctx.expr(0))  # Ejecutar la expresión de inicialización

        # Evaluar la condición antes de entrar al bucle
        while self.visit(ctx.expr(1)):  # Evaluar la condición en cada iteración
            # Ejecutar el bloque dentro del for
            self.visit(ctx.bloque())  

            # Actualizar la variable de control
            self.visit(ctx.expr(2))  

        return None  # El bloque for no devuelve un valor directamente

 
    def visitReasignacion(self, ctx: ExprParser.ReasignacionContext):
        var_name = ctx.VARIABLE().getText()  # Obtener el nombre de la variable
        new_value = self.visit(ctx.expr())  # Obtener el nuevo valor a asignar a la variable

        if var_name in self.variables:  # Verificar si la variable ya está definida
            original_value = self.variables[var_name]  # Obtener el valor original de la variable

            # Validación "insana" del tipo
            if isinstance(original_value, int) and not isinstance(new_value, int):
                raise TypeError(f"Error de tipo: La variable '{var_name}' es de tipo 'int', pero se intentó asignar un valor de tipo {type(new_value)}")
            elif isinstance(original_value, float) and not isinstance(new_value, float):
                raise TypeError(f"Error de tipo: La variable '{var_name}' es de tipo 'float', pero se intentó asignar un valor de tipo {type(new_value)}")
            else:
                # Si el tipo coincide, realizar la reasignación
                print(f"Reasignando {var_name} a {new_value}")
                self.variables[var_name] = new_value  # Actualizar el valor de la variable
        else:
            raise NameError(f"Variable no definida: {var_name}")

        return new_value  # Retornar el nuevo valor asignado
 
       # Visit a parse tree produced by ExprParser#declaracion.
    def visitDeclaracion(self, ctx: ExprParser.DeclaracionContext):
        var_name = ctx.VARIABLE().getText()  # Obtener el nombre de la variable
        var_type = ctx.tipo().getText()  # Obtener el tipo de la variable
        value = self.visit(ctx.expr())  # Obtener el valor de la expresión

        # Validación "insana" del tipo
        if var_type == "entero":
            if not isinstance(value, int):
                raise TypeError(f"Error de tipo: Se esperaba un valor de tipo 'int' para la variable '{var_name}', pero se obtuvo {traducir_tipo(type(value))}")
        elif var_type == "decimal":
            if not isinstance(value, float):
                raise TypeError(f"Error de tipo: Se esperaba un valor de tipo 'float' para la variable '{var_name}', pero se obtuvo {traducir_tipo(type(value))}")
        else:
            raise TypeError(f"Tipo de variable no soportado: {var_type}")

        # Asignar el valor a la variable si pasa la validación
        self.variables[var_name] = value
        return value  # Retornar el valor de la asignación

    # Visit a parse tree produced by ExprParser#sentencia.
    def visitSentencia(self, ctx:ExprParser.SentenciaContext):
        return self.visitChildren(ctx)
 
    # Visit a parse tree produced by ExprParser#tipo.
    def visitTipo(self, ctx:ExprParser.TipoContext):
        return self.visitChildren(ctx)

   # Visit a parse tree produced by ExprParser#actualizacion.
    def visitActualizacion(self, ctx:ExprParser.ActualizacionContext):
        var_name = ctx.VARIABLE().getText()

        if var_name not in self.variables:
            raise NameError(f"Variable no definida: {var_name}")

        if ctx.MASMAS():  # Manejar 'x++'
            self.variables[var_name] += 1
        elif ctx.MENOSMENOS():  # Manejar 'x--'
            self.variables[var_name] -= 1
        elif ctx.expr():  
                new_value = self.visit(ctx.expr())  
                self.variables[var_name] = new_value  
      
        return self.variables[var_name]
    
    # Visit a parse tree produced by ExprParser#sentencia_if.
    def visitSentencia_if(self, ctx: ExprParser.Sentencia_ifContext):
        # Comprobar si bloque_condicional es una lista
        bloques_condicionales = ctx.bloque_condicional()
        if isinstance(bloques_condicionales, list):
            condition_value = self.visit(bloques_condicionales[0].expr())  # Accede al primer bloque
        else:
            condition_value = self.visit(bloques_condicionales.expr())  # Si no es lista, accede directamente
        
        if condition_value:
            self.visit(ctx.bloque_condicional().bloque_de_sentencia())
        else:
            if ctx.ELSE():
                self.visit(ctx.bloque_de_sentencia())
            for elif_block in ctx.ELSEIF():
                elif_condition = self.visit(elif_block.bloque_condicional().expr())
                if elif_condition:
                    self.visit(elif_block.bloque_condicional().bloque_de_sentencia())
                    break

 
    # Visit a parse tree produced by ExprParser#sentencia_while.
    def visitSentencia_while(self, ctx: ExprParser.Sentencia_whileContext):
    # Evaluar la condición antes de entrar al bucle
        while self.visit(ctx.expr()):  # Mientras la condición sea verdadera
            # Ejecutar el bloque de sentencias dentro del while
            self.visit(ctx.bloque_de_sentencia())
 
 
    # Visit a parse tree produced by ExprParser#sentencia_for.
    def visitSentencia_for(self, ctx: ExprParser.Sentencia_forContext):
        # Primero ejecutamos la declaración (asignación)
        self.visit(ctx.declaracion())
    
        # Condición del ciclo
        while self.visit(ctx.expr()):
            # Ejecutamos el bloque dentro del for
            self.visit(ctx.bloque_de_sentencia())
            # Realizamos el incremento/decremento de la variable en el ciclo
            self.visit(ctx.actualizacion())  # Actualización de la variable de control
 
 
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
   # Operadores de comparación
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