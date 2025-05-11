from ExprVisitor import ExprVisitor
from ExprParser import ExprParser
# Visitors modularizados
from visitors.ExprBaseVisitor import *
from visitors.ExprStatementVisitor import *

def traducir_tipo(tipo):
    return ExprBaseVisitor.traducir_tipo(tipo)


class PersonalizatedVisitor( ExprStatementVisitor, ExprVisitor):
    def __init__(self):
        super().__init__()


    # Visit a parse tree produced by ExprParser#gramatica.
    def visitGramatica(self, ctx:ExprParser.GramaticaContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#programa.
    def visitPrograma(self, ctx: ExprParser.ProgramaContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#bloque.
    def visitBloque(self, ctx:ExprParser.BloqueContext):
        self.enter_scope()  # Inicia un nuevo ámbito local
        result = self.visitChildren(ctx)
        self.exit_scope()   # Finaliza el ámbito local
        return result

    def visitTipo(self, ctx:ExprParser.TipoContext):
        return self.visitChildren(ctx)

    def visitActualizacion(self, ctx: ExprParser.ActualizacionContext):
        return super().visitActualizacion(ctx)

    # Visit a parse tree produced by ExprParser#sentencia.
    def visitSentencia(self, ctx: ExprParser.SentenciaContext):
        return super().visitSentencia(ctx)

    def visitDeclaracion_funcion(self, ctx:ExprParser.Declaracion_funcionContext):
        return super().visitDeclaracion_funcion( ctx)

    # Visit a parse tree produced by ExprParser#funcion_llamada.
    def visitFuncion_llamada(self, ctx:ExprParser.Funcion_llamadaContext):
        return super().visitFuncion_llamada(ctx)

    # Visit a parse tree produced by ExprParser#parametros.
    def visitParametros(self, ctx:ExprParser.ParametrosContext):
        return super().visitParametros(ctx)

    # Visit a parse tree produced by ExprParser#parametro.
    def visitParametro(self, ctx:ExprParser.ParametroContext):
        return super().visitParametro( ctx)

    # Visit a parse tree produced by ExprParser#argumentos.
    def visitArgumentos(self, ctx:ExprParser.ArgumentosContext):
        return super().visitArgumentos( ctx)

    def visitSentencia_if(self, ctx: ExprParser.Sentencia_ifContext):
        return super().visitSentencia_if( ctx)

    def visitBloque_de_sentencia(self, ctx: ExprParser.Bloque_de_sentenciaContext):
        return super().visitBloque_de_sentencia(ctx)

    def visitSentencia_while(self, ctx: ExprParser.Sentencia_whileContext):
        return super().visitSentencia_while( ctx)

    def visitSentencia_for(self, ctx: ExprParser.Sentencia_forContext):
        return super().visitSentencia_for( ctx)

    def visitBloque_condicional(self, ctx:ExprParser.Bloque_condicionalContext):
        return super().visitBloque_condicional(ctx)

    def visitDeclaracion(self, ctx: ExprParser.DeclaracionContext):
        super().visitDeclaracion(ctx)

    def visitReasignacion(self, ctx: ExprParser.ReasignacionContext):
        super().visitReasignacion(ctx)

    def visitFuncion_llamada_expr(self, ctx:ExprParser.Funcion_llamada_exprContext):
        return super().visitChildren(ctx) 

    def visitRetorna(self, ctx:ExprParser.RetornaContext):
        super().visitRetorna(ctx)

    def visitDeclaracion_sin_asignacion(self, ctx:ExprParser.Declaracion_sin_asignacionContext):
        super().visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#mostrar.
    def visitMostrar(self, ctx:ExprParser.MostrarContext):
        value = self.visit(ctx.expr())
        print(value)


    def visitExpr(self, ctx: ExprParser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))

        left = self.visit(ctx.getChild(0))
        operator = ctx.getChild(1)
        right = self.visit(ctx.getChild(2))

        # print(f"Variable L E: {left}")
        # print(f"Variable R E: {right}")
        # print(f"Operador R E: {operator.getText()}")

        if operator.getText() == '+':
            # Verificar si ambos operandos son cadenas
            if isinstance(left, str) and isinstance(right, str):
                result = left + right  # Concatenación de cadenas
            elif isinstance(left, int) and isinstance(right, int):
                result = left + right  # Suma numérica
            else:
                raise ValueError(f"Operación no permitida entre tipos {type(left)} y {type(right)} para el operador '+'")
        elif operator.getText() == '-':
            result = left - right
        elif operator.getText() == '<':
            result = left < right
        elif operator.getText() == '>':
            result = left > right
        elif operator.getText() == '<=':
            result = left <= right
        elif operator.getText() == '>=':
            result = left >= right
        elif operator.getText() == '==':
            result = left == right
        elif operator.getText() == '!=':
            result = left != right
        else:
            raise ValueError(f"Operador desconocido {operator.getText()}")

        # print(f"Resultado de la evaluación: {result}")
        return result


    def visitTerm(self, ctx: ExprParser.TermContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))

        left = self.visit(ctx.getChild(0))
        operator = ctx.getChild(1)
        right = self.visit(ctx.getChild(2))

        # print(f" Variable L T: {left}")
        # print(f" Variable R T: {right}")
        if operator.getText() == '*':
            return left * right
        elif operator.getText() == '/':
            if right == 0:
                raise ZeroDivisionError("División por cero no permitida")
            return left / right
        else:
            raise ValueError(f"Operador desconocido {operator.getText()}")

    def visitFactor(self, ctx: ExprParser.FactorContext):
        if ctx.NUMERO():
            return int(ctx.NUMERO().getText())
        elif ctx.DECIMAL():
            return float(ctx.DECIMAL().getText())
        elif ctx.BOOLEANO():
            return ctx.BOOLEANO().getText() == "verdadero"
        elif ctx.CADENA():
            return ctx.CADENA().getText()[1:-1]  # Elimina las comillas
        elif ctx.VARIABLE():
            var_name = ctx.VARIABLE().getText()
            return super().get_variable(var_name)
        elif ctx.PARENTESIS_INICIAL():
            return self.visit(ctx.getChild(1))
        elif ctx.MENOS():
            return -self.visit(ctx.getChild(1))
        elif ctx.funcion_llamada_expr():  # Llamada a función como expresión
            return self.visit(ctx.funcion_llamada_expr())        
        else:
            raise ValueError("Operación no soportada")
