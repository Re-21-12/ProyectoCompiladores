from ExprParser import ExprParser
from visitors.ExprBaseVisitor import *

class ExprFunctionsVisitor(ExprBaseVisitor):
    def __init__(self):
        super().__init__()
        self.return_value = None
        self.should_return = False

    def visitFuncion_llamada_expr(self, ctx: ExprParser.Funcion_llamada_exprContext):
        """Handle function calls within expressions"""
        return self._execute_function_call(ctx)

    def visitDeclaracion_funcion(self, ctx: ExprParser.Declaracion_funcionContext):
        """Store function definition with name, return type, parameters, body, and return statement"""
        nombre = ctx.VARIABLE().getText()
        tipo_retorno = ctx.tipo().getText()
        parametros = self.visitParametros(ctx.parametros()) if ctx.parametros() else []
        cuerpo = ctx.bloque()
        retorno = ctx.retorna()  # Can be None if no explicit return

        self.funciones[nombre] = {
            "tipo_retorno": tipo_retorno,
            "parametros": parametros,
            "cuerpo": cuerpo,
            "retorno": retorno
        }
        return None

    def visitRetorna(self, ctx: ExprParser.RetornaContext):
        """Handle return statements, setting the return value and flag"""
        self.return_value = self.visit(ctx.expr())
        self.should_return = True
        return self.return_value

    def visitArgumentos(self, ctx: ExprParser.ArgumentosContext):
        """Process function arguments"""
        return [self.visit(expr) for expr in ctx.expr()] if ctx.expr() else []

    def visitFuncion_llamada(self, ctx: ExprParser.Funcion_llamadaContext):
        """Execute a function call as a statement"""
        self._execute_function_call(ctx)
        return None

    def _execute_function_call(self, ctx):
        """Common function call execution logic"""
        nombre = ctx.VARIABLE().getText()
        
        if nombre not in self.funciones:
            raise Exception(f"Función '{nombre}' no definida")

        funcion = self.funciones[nombre]
        argumentos = self.visit(ctx.argumentos()) if ctx.argumentos() else []
        
        # Parameter count validation
        if len(argumentos) != len(funcion["parametros"]):
            raise Exception(f"Número incorrecto de argumentos para '{nombre}'")

        # Save current state
        old_return = self.return_value
        old_should_return = self.should_return
        self.return_value = None
        self.should_return = False

        # Enter new scope
        self.enter_scope()
        
        # Assign parameters with type checking
        for param_info, arg in zip(funcion["parametros"], argumentos):
            self.define_variable(param_info["nombre"], arg)

        # Execute function body
        if funcion["cuerpo"]:
            self.visit(funcion["cuerpo"])

        # Handle explicit return if not already encountered
        if not self.should_return and funcion["retorno"]:
            self.visit(funcion["retorno"])

        # Exit scope
        self.exit_scope()

        # Restore state and return value
        result = self.return_value
        self.return_value = old_return
        self.should_return = old_should_return

        return result

    def visitBloque(self, ctx: ExprParser.BloqueContext):
        """Execute statements in block, stopping if return encountered"""
        for sentencia in ctx.sentencia():
            self.visit(sentencia)
            if self.should_return:
                break
        return self.return_value if self.should_return else None

    def visitSentencia_if(self, ctx: ExprParser.Sentencia_ifContext):
        """Handle if statements with proper return handling"""
        # Main if
        if self.visit(ctx.bloque_condicional(0)):
            return self.visit(ctx.bloque_de_sentencia()[0])  # Access the first block correctly
        
        # Else ifs
        for i in range(1, len(ctx.bloque_condicional())):
            if self.visit(ctx.bloque_condicional(i)):
                return self.visit(ctx.bloque_de_sentencia()[i])  # Access the blocks using indices correctly
        
        # Else
        if ctx.ELSE():
            return self.visit(ctx.bloque_de_sentencia()[-1])  # Access the last block for else

        return None

    
    def visitParametros(self, ctx: ExprParser.ParametrosContext):
        """Process function parameters with their types"""
        return [self.visit(param) for param in ctx.parametro()]

    def visitParametro(self, ctx: ExprParser.ParametroContext):
        """Extract parameter name and type"""
        return {
            "nombre": ctx.VARIABLE().getText(),
            "tipo": ctx.tipo().getText()
        }