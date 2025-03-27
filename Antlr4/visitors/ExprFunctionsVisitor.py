from visitors.ExprBaseVisitor import *
from ExprParser import ExprParser

class ExprFunctionsVisitor(ExprBaseVisitor):
    def visitDeclaracion_funcion(self, ctx: ExprParser.Declaracion_funcionContext):
        """Guarda la función en el diccionario con su nombre, parámetros y bloque"""
        nombre = ctx.VARIABLE().getText()
        tipo = ctx.tipo().getText()  # Tipo de retorno
        parametros = self.visitParametros(ctx.parametros()) if ctx.parametros() else []
        cuerpo = ctx.bloque()
        retorna = ctx.expr()

        # Guardar la función en el diccionario de funciones
        self.funciones[nombre] = {
            "tipo": tipo,
            "parametros": parametros,
            "cuerpo": cuerpo,
            "retorna": retorna
        }
        return None  # No ejecuta la función en este punto, solo la almacena

    def visitParametros(self, ctx: ExprParser.ParametrosContext):
        """Devuelve una lista de los nombres de los parámetros"""
        return [self.visitParametro(param) for param in ctx.parametro()]

    def visitParametro(self, ctx: ExprParser.ParametroContext):
        """Obtiene el nombre del parámetro"""
        return ctx.VARIABLE().getText()  # Devuelve el nombre del parámetro

    def visitFuncion_llamada(self, ctx: ExprParser.Funcion_llamadaContext):
        """Ejecuta una función almacenada usando los argumentos pasados"""
        nombre = ctx.VARIABLE().getText()
        argumentos = self.visitArgumentos(ctx.argumentos()) if ctx.argumentos() else []

        # Verificar si la función está definida
        if nombre not in self.funciones:
            raise Exception(f"Error: la función '{nombre}' no está definida.")

        funcion = self.funciones[nombre]
        parametros = funcion["parametros"]

        if len(parametros) != len(argumentos):
            raise Exception(f"Error: la función '{nombre}' espera {len(parametros)} argumentos, pero recibió {len(argumentos)}.")

        # Guardar el contexto local de la función en el ámbito actual
        ExprBaseVisitor.enter_scope(self)
        for param, arg in zip(parametros, argumentos):
            ExprBaseVisitor.define_variable(self, param, arg)

        # Ejecutar el cuerpo de la función
        resultado = self.visit(funcion["retorna"])  # Evaluar la expresión de retorno

        # Salir del ámbito local
        ExprBaseVisitor.exit_scope(self)

        return resultado

    def visitArgumentos(self, ctx: ExprParser.ArgumentosContext):
        """Obtiene los valores de los argumentos pasados en la llamada de la función"""
        return [self.visit(expr) for expr in ctx.expr()]

