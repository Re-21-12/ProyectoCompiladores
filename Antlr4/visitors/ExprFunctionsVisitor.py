from ExprParser import ExprParser
from visitors.ExprBaseVisitor import *

class ExprFunctionsVisitor(ExprBaseVisitor):
    def __init__(self):
        super().__init__()
        self.return_value = None
        self.should_return = False

    def visitFuncion_llamada_expr(self, ctx:ExprParser.Funcion_llamada_exprContext):
        return self.visitChildren(ctx)    

    def visitDeclaracion_funcion(self, ctx: ExprParser.Declaracion_funcionContext):
        """Guarda la función en el diccionario con su nombre, parámetros, cuerpo y retorno"""
        nombre = ctx.VARIABLE().getText()
        tipo = ctx.tipo().getText()
        parametros = self.visitParametros(ctx.parametros()) if ctx.parametros() else []
        cuerpo = ctx.bloque()
        retorno = ctx.retorna()  # Puede ser None si no hay retorno explícito

        self.funciones[nombre] = {
            "tipo": tipo,
            "parametros": parametros,
            "cuerpo": cuerpo,
            "retorno": retorno
        }
        return None

    def visitRetorna(self, ctx: ExprParser.RetornaContext):
        """Maneja una sentencia de retorno, estableciendo el valor y marcando para retornar"""
        self.return_value = self.visit(ctx.expr())
        self.should_return = True
        return self.return_value

    def visitFuncion_llamada(self, ctx: ExprParser.Funcion_llamadaContext):
        """Ejecuta una función almacenada"""
        nombre = ctx.VARIABLE().getText()
        
        if nombre not in self.funciones:
            raise Exception(f"Función '{nombre}' no definida")

        funcion = self.funciones[nombre]
        argumentos = self.visitArgumentos(ctx.argumentos()) if ctx.argumentos() else []

        # Verificación de parámetros
        if len(argumentos) != len(funcion["parametros"]):
            raise Exception(f"Número incorrecto de argumentos para '{nombre}'")

        # Guardar estado actual
        old_return = self.return_value
        old_should_return = self.should_return
        self.return_value = None
        self.should_return = False

        # Entrar en nuevo ámbito
        self.enter_scope()
        
        # Asignar parámetros
        for param, arg in zip(funcion["parametros"], argumentos):
            self.define_variable(param, arg)

        # Ejecutar cuerpo de la función
        if funcion["cuerpo"]:
            self.visit(funcion["cuerpo"])

        # Si no hubo retorno explícito, visitar el retorno declarado (si existe)
        if not self.should_return and funcion["retorno"]:
            self.visit(funcion["retorno"])

        # Salir del ámbito
        self.exit_scope()

        # Restaurar estado y devolver valor
        result = self.return_value
        print(f"Resultado de '{nombre}': {result} (tipo: {type(result).__name__})")
        self.return_value = old_return
        self.should_return = old_should_return

        return result

    def visitBloque(self, ctx: ExprParser.BloqueContext):
        """Visita cada sentencia en el bloque, deteniéndose si hay un retorno"""
        for sentencia in ctx.sentencia():
            self.visit(sentencia)
            if self.should_return:
                break
        return self.return_value if self.should_return else None

    def visitSentencia_if(self, ctx: ExprParser.Sentencia_ifContext):
        """Visita un bloque if, manejando correctamente los retornos"""
        # Visitar if principal
        condicion = self.visit(ctx.bloque_condicional(0))
        if condicion:
            return self.visit(ctx.bloque_de_sentencia(0))
        
        # Visitar else ifs
        for i in range(1, len(ctx.bloque_condicional())):
            condicion = self.visit(ctx.bloque_condicional(i))
            if condicion:
                return self.visit(ctx.bloque_de_sentencia(i))
        
        # Visitar else si existe
        if ctx.ELSE():
            return self.visit(ctx.bloque_de_sentencia(-1))
        
        return None