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
            print("llego")
            return self.visitRetorna(ctx.retorna())
        elif ctx.declaracion_sin_asignacion():
            return self.visitDeclaracion_sin_asignacion(ctx.declaracion_sin_asignacion())
        else:
            print(f"DEBUG: Unrecognized statement context: {dir(ctx)}")
            print(f"DEBUG: Statement text: {ctx.getText()}")
            raise ValueError(f"Sentencia no reconocida: {ctx.getText()}")

    def visitSentencia_if(self, ctx: ExprParser.Sentencia_ifContext):
        """Handle if-elif-else statements with proper return value propagation"""
        # Evaluate main if condition
        if self._evaluate_condition(ctx.bloque_condicional(0)):
            return self._execute_block(ctx.bloque_de_sentencia(0))
        
        # Evaluate elif conditions
        for i in range(1, len(ctx.bloque_condicional())):
            if self._evaluate_condition(ctx.bloque_condicional(i)):
                return self._execute_block(ctx.bloque_de_sentencia(i))
        
        # Evaluate else block if present
        if ctx.ELSE():
            return self._execute_block(ctx.bloque_de_sentencia(-1))
        
        return None

    def _evaluate_condition(self, cond_block: ExprParser.Bloque_condicionalContext):
        """Helper to evaluate a condition block"""
        return self.visit(cond_block.expr())

    def _execute_block(self, block: ExprParser.Bloque_de_sentenciaContext):
        """Helper to execute a block and handle return statements"""
        result = self.visit(block)
        return result if self.should_return else None

    def visitBloque_de_sentencia(self, ctx: ExprParser.Bloque_de_sentenciaContext):
        """Execute statements in a block (either single statement or {block})"""
        if ctx.sentencia():  # Single statement
            return self.visit(ctx.sentencia())
        else:  # Block with {}
            return self.visit(ctx.bloque())

    def visitSentencia_while(self, ctx: ExprParser.Sentencia_whileContext):
        """Execute while loop with proper break on return"""
        cond_block = ctx.bloque_condicional()
        while self._evaluate_condition(cond_block):
            result = self._execute_block(cond_block.bloque_de_sentencia())
            if self.should_return:
                return result

    def visitRetorna(self, ctx:ExprParser.RetornaContext):
        return super().visitRetorna(ctx)

    def visitSentencia_for(self, ctx: ExprParser.Sentencia_forContext):
        """Execute for loop with proper initialization, condition, and update"""
        # Initialization
        self.visit(ctx.declaracion())
        
        # Loop while condition is true
        while self.visit(ctx.expr()):
            # Execute body
            result = self._execute_block(ctx.bloque_de_sentencia())
            if self.should_return:
                return result
            
            # Update step
            self.visit(ctx.actualizacion())

    def visitMostrar(self, ctx: ExprParser.MostrarContext):
        """Handle print statement"""
        value = self.visit(ctx.expr())
        print(value)  # Simple print without debug prefix

    # Inherited methods with proper type hints
    def visitDeclaracion_funcion(self, ctx: ExprParser.Declaracion_funcionContext):
        return super().visitDeclaracion_funcion(ctx)

    def visitFuncion_llamada(self, ctx: ExprParser.Funcion_llamadaContext):
        return super().visitFuncion_llamada(ctx)

    def visitParametros(self, ctx: ExprParser.ParametrosContext):
        return super().visitParametros(ctx)

    def visitParametro(self, ctx: ExprParser.ParametroContext):
        return super().visitParametro(ctx)

    def visitArgumentos(self, ctx: ExprParser.ArgumentosContext):
        return super().visitArgumentos(ctx)

    def visitBloque_condicional(self, ctx: ExprParser.Bloque_condicionalContext):
        return super().visitBloque_condicional(ctx)