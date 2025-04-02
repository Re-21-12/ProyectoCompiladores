from ExprParser import ExprParser
from visitors.ExprFunctionsVisitor import *
from visitors.ExprVariableVisitor import *


class ExprStatementVisitor( ExprFunctionsVisitor, ExprVariableVisitor):

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
            print("mostrando mostrar")
            return self.visitMostrar(ctx.mostrar())
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
    def visitBloque_de_sentencia(self, ctx:ExprParser.Bloque_de_sentenciaContext):
        return self.visitChildren(ctx)


    def visitBloque_condicional(self, ctx:ExprParser.Bloque_condicionalContext):
        return self.visitChildren(ctx)
    
    def visitSentencia_while(self, ctx: ExprParser.Sentencia_whileContext):
        while self.visit(ctx.bloque_condicional().expr()):
            self.visit(ctx.bloque_condicional().bloque_de_sentencia())

    # Visit a parse tree produced by ExprParser#sentencia_for.
    def visitSentencia_for(self, ctx: ExprParser.Sentencia_forContext):
        self.visit(ctx.declaracion())
        while self.visit(ctx.expr()):
            self.visit(ctx.bloque_de_sentencia())
            self.visit(ctx.actualizacion())
                
    def visitMostrar(self, ctx:ExprParser.MostrarContext):
        value = self.visit(ctx.expr())
        print("[INFO]: " , value)

