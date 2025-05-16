from ExprParser import ExprParser
from visitors.ExprFunctionsVisitor import *
from visitors.ExprVariableVisitor import *

class ExprStatementVisitor(ExprFunctionsVisitor, ExprVariableVisitor):

    def visitSentencia(self, ctx: ExprParser.SentenciaContext):
        """Dispatch to appropriate statement visitor method"""
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
        elif ctx.declaracion_funcion():
            return self.visitDeclaracion_funcion(ctx.declaracion_funcion())
        elif ctx.funcion_llamada():
            return self.visitFuncion_llamada(ctx.funcion_llamada())
        elif ctx.retorna():
            return self.visitRetorna(ctx.retorna())
        elif ctx.declaracion_sin_asignacion():
            return self.visitDeclaracion_sin_asignacion(ctx.declaracion_sin_asignacion())
        else:
            raise ValueError(f"Sentencia no reconocida: {ctx.getText()}")

    def visitSentencia_if(self, ctx: ExprParser.Sentencia_ifContext):
        bloques = ctx.bloque_de_sentencia()
        if not isinstance(bloques, list):
            bloques = [bloques]

        condiciones = ctx.bloque_condicional()
        if not isinstance(condiciones, list):
            condiciones = [condiciones]

        # Main if
        if self.visit(condiciones[0]):
            if len(bloques) > 0:
                self.enter_scope()
                result = self.visit(bloques[0])
                self.exit_scope()
                return result

        # Else ifs
        for i in range(1, len(condiciones)):
            if self.visit(condiciones[i]):
                if len(bloques) > i:
                    self.enter_scope()
                    result = self.visit(bloques[i])
                    self.exit_scope()
                    return result

        # Else
        if ctx.ELSE():
            if len(bloques) > len(condiciones):
                self.enter_scope()
                result = self.visit(bloques[-1])
                self.exit_scope()
                return result

        return None


    def visitSentencia_while(self, ctx: ExprParser.Sentencia_whileContext):
        cond_block = ctx.bloque_condicional()
        while self._evaluate_condition(cond_block):
            self.enter_scope()
            result = self._execute_block(cond_block.bloque_de_sentencia())
            self.exit_scope()
            if self.should_return:
                return result

    def visitSentencia_for(self, ctx: ExprParser.Sentencia_forContext):
        # Scope para todo el for
        self.enter_scope()
        self.visit(ctx.declaracion())

        while self.visit(ctx.expr()):
            self.enter_scope()
            result = self._execute_block(ctx.bloque_de_sentencia())
            self.exit_scope()
            if self.should_return:
                self.exit_scope()
                return result
            self.visit(ctx.actualizacion())

        self.exit_scope()

    def visitMostrar(self, ctx: ExprParser.MostrarContext):
        value = self.visit(ctx.expr())
        print(value)

    def visitBloque_de_sentencia(self, ctx: ExprParser.Bloque_de_sentenciaContext):
        if ctx.sentencia():
            return self.visit(ctx.sentencia())
        else:
            return self.visit(ctx.bloque())

    def visitRetorna(self, ctx: ExprParser.RetornaContext):
        return super().visitRetorna(ctx)

    def _evaluate_condition(self, cond_block: ExprParser.Bloque_condicionalContext):
        return self.visit(cond_block.expr())

    def _execute_block(self, block: ExprParser.Bloque_de_sentenciaContext):
        result = self.visit(block)
        return result if self.should_return else None

    # Inherited methods with proper cleanup
    def visitDeclaracion_funcion(self, ctx: ExprParser.Declaracion_funcionContext):
        return super().visitDeclaracion_funcion(ctx)

    def visitFuncion_llamada(self, ctx: ExprParser.Funcion_llamadaContext):
        # Scope de ejecución de la función ya se maneja en el visitor base
        result = super().visitFuncion_llamada(ctx)
        self.should_return = False
        self.return_value = None
        return result

    def visitParametros(self, ctx: ExprParser.ParametrosContext):
        return super().visitParametros(ctx)

    def visitParametro(self, ctx: ExprParser.ParametroContext):
        return super().visitParametro(ctx)

    def visitArgumentos(self, ctx: ExprParser.ArgumentosContext):
        return super().visitArgumentos(ctx)

    def visitBloque_condicional(self, ctx: ExprParser.Bloque_condicionalContext):
        return super().visitBloque_condicional(ctx)
