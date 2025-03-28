from ExprParser import ExprParser
from visitors.ExprFunctionsVisitor import *

class ExprStatementVisitor( ExprFunctionsVisitor):

    def visitSentencia(self, ctx: ExprParser.SentenciaContext):
        if ctx.sentencia_if():
            return self.visitSentencia_if(ctx.sentencia_if())
        elif ctx.sentencia_while():
            return self.visitSentencia_while(ctx.sentencia_while())
        elif ctx.sentencia_for():
            return self.visitSentencia_for(ctx.sentencia_for())
        elif ctx.reasignacion():
            return self.visitReasignacion(ctx.reasignacion())
        elif ctx.mostrar():
            print("mostrando mostrar")
            return self.visitMostrar(ctx.mostrar())
        elif ctx.declaracion():
            return self.visitDeclaracion(ctx.declaracion())
        elif ctx.actualizacion():
            return self.visitActualizacion(ctx.actualizacion())
        elif ctx.declaracion_funcion():
            return self.visit(ctx.declaracion_funcion())
        elif ctx.funcion_llamada():
            return self.visitFuncion_llamada(ctx.funcion_llamada())
        else:
            raise ValueError("Sentencia no reconocida")
        
    def visitDeclaracion_funcion(self, ctx:ExprParser.Declaracion_funcionContext):
        return super().visitDeclaracion_funcion(ctx)

    # Visit a parse tree produced by ExprParser#funcion_llamada.
    def visitFuncion_llamada(self, ctx:ExprParser.Funcion_llamadaContext):
        return super().visitFuncion_llamada(ctx)

    # Visit a parse tree produced by ExprParser#parametros.
    def visitParametros(self, ctx:ExprParser.ParametrosContext):
        return super().visitParametros(ctx)

    # Visit a parse tree produced by ExprParser#parametro.
    def visitParametro(self, ctx:ExprParser.ParametroContext):
        return super().visitParametro(ctx)

    # Visit a parse tree produced by ExprParser#argumentos.
    def visitArgumentos(self, ctx:ExprParser.ArgumentosContext):
        return super().visitArgumentos(ctx)
    
    def visitSentencia_if(self, ctx: ExprParser.Sentencia_ifContext):
        # Obtener todos los bloques condicionales (if + elifs)
        bloques_condicionales = ctx.bloque_condicional()
        
        # Procesar el IF principal
        if not bloques_condicionales:  # Por si acaso no hay bloques
            return None
        
        # Evaluar condición del IF
        first_condition = self.visit(bloques_condicionales[0].expr())
        print(f"Condición del if: {first_condition}")
        
        if first_condition:
            # Ejecutar bloque del IF y retornar su resultado
            return self.visit(bloques_condicionales[0].bloque_de_sentencia())
        
        # Procesar ELIFs si existen
        for i in range(1, len(bloques_condicionales)):
            elif_condition = self.visit(bloques_condicionales[i].expr())
            print(f"Condición elif [{i}]: {elif_condition}")
            if elif_condition:
                # Ejecutar bloque del ELIF y retornar su resultado
                return self.visit(bloques_condicionales[i].bloque_de_sentencia())
        
        # Procesar ELSE si existe
        if ctx.ELSE():
            print("Ejecutando bloque ELSE")
            return self.visit(ctx.bloque_de_sentencia())
        
        return None

    def visitSentencia_while(self, ctx: ExprParser.Sentencia_whileContext):
        while self.visit(ctx.bloque_condicional().expr()):
            self.visit(ctx.bloque_condicional().bloque_de_sentencia())

    def visitSentencia_for(self, ctx: ExprParser.Sentencia_forContext):
        print("Visita de declaracion del for")
        self.visit(ctx.declaracion())  # Visita la declaración
        print(f"Condición de for: {ctx.expr()}")
        while self.visit(ctx.expr()):  # Evalúa la condición del ciclo
            print(f"Ejecutando bloque del for: {ctx.bloque_de_sentencia()}")
            self.visit(ctx.bloque_de_sentencia())  # Ejecuta el bloque
            self.visit(ctx.actualizacion())  # Ejecuta la actualización
                
        # Visit a parse tree produced by ExprParser#mostrar.
    def visitMostrar(self, ctx:ExprParser.MostrarContext):
        value = self.visit(ctx.expr())
        print(value)
        return value  

