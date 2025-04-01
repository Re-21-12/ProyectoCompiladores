class ASTNode:
    def __init__(self, type, children=None, value=None):
        self.type = type
        self.children = children if children else []
        self.value = value

    def __repr__(self):
        return f"ASTNode(type={self.type}, value={self.value}, children={self.children})"

from ExprParser import ExprParser
from ExprVisitor import ExprVisitor

class ASTVisitor(ExprVisitor):
    def visitGramatica(self, ctx: ExprParser.GramaticaContext):
        return ASTNode("Gramatica", children=[self.visit(child) for child in ctx.children])

    def visitPrograma(self, ctx: ExprParser.ProgramaContext):
        return ASTNode("Programa", children=[self.visit(child) for child in ctx.children])

    def visitBloque(self, ctx: ExprParser.BloqueContext):
        return ASTNode("Bloque", children=[self.visit(child) for child in ctx.children])

    def visitSentencia(self, ctx: ExprParser.SentenciaContext):
        return ASTNode("Sentencia", children=[self.visit(child) for child in ctx.children])

    def visitSentencia_if(self, ctx: ExprParser.Sentencia_ifContext):
        cond = self.visit(ctx.bloque_condicional().expr())
        bloque = self.visit(ctx.bloque_de_sentencia())
        else_block = self.visit(ctx.bloque_de_sentencia()) if ctx.ELSE() else None
        return ASTNode("If", children=[cond, bloque] + [else_block] if else_block else [])

    def visitSentencia_while(self, ctx: ExprParser.Sentencia_whileContext):
        cond = self.visit(ctx.bloque_condicional().expr())
        bloque = self.visit(ctx.bloque_de_sentencia())
        return ASTNode("While", children=[cond, bloque])

    def visitSentencia_for(self, ctx: ExprParser.Sentencia_forContext):
        inicio = self.visit(ctx.declaracion()) if ctx.declaracion() else None
        cond = self.visit(ctx.expr())
        actualizacion = self.visit(ctx.actualizacion())
        bloque = self.visit(ctx.bloque_de_sentencia())
        return ASTNode("For", children=[inicio, cond, actualizacion, bloque])

    def visitDeclaracion_funcion(self, ctx: ExprParser.Declaracion_funcionContext):
        tipo = self.visit(ctx.tipo())
        nombre = ctx.VARIABLE().getText()
        parametros = [self.visit(param) for param in ctx.parametros().parametro()]
        bloque = self.visit(ctx.bloque())
        retorno = self.visit(ctx.expr()) if ctx.expr() else None
        return ASTNode("DeclaracionFuncion", children=[tipo] + parametros + [bloque, retorno], value=nombre)

    def visitFuncion_llamada(self, ctx: ExprParser.Funcion_llamadaContext):
        nombre = ctx.VARIABLE().getText()
        argumentos = [self.visit(arg) for arg in ctx.argumentos().expr()]
        return ASTNode("FuncionLlamada", children=argumentos, value=nombre)

    def visitParametros(self, ctx: ExprParser.ParametrosContext):
        return ASTNode("Parametros", children=[self.visit(child) for child in ctx.children])

    def visitParametro(self, ctx: ExprParser.ParametroContext):
        return ASTNode("Parametro", children=[self.visit(child) for child in ctx.children])

    def visitArgumentos(self, ctx: ExprParser.ArgumentosContext):
        return ASTNode("Argumentos", children=[self.visit(arg) for arg in ctx.expr()])

    def visitBloque_condicional(self, ctx: ExprParser.Bloque_condicionalContext):
        return ASTNode("BloqueCondicional", children=[self.visit(child) for child in ctx.children])

    def visitBloque_de_sentencia(self, ctx: ExprParser.Bloque_de_sentenciaContext):
        return ASTNode("BloqueSentencia", children=[self.visit(child) for child in ctx.children])

    def visitDeclaracion(self, ctx: ExprParser.DeclaracionContext):
        tipo = self.visit(ctx.tipo())
        nombre = ctx.VARIABLE().getText()
        valor = self.visit(ctx.expr()) if ctx.expr() else None
        return ASTNode("Declaracion", children=[tipo, valor], value=nombre)

    def visitReasignacion(self, ctx: ExprParser.ReasignacionContext):
        nombre = ctx.VARIABLE().getText()
        valor = self.visit(ctx.expr())
        return ASTNode("Reasignacion", children=[valor], value=nombre)

    def visitTipo(self, ctx: ExprParser.TipoContext):
        return ASTNode("Tipo", value=ctx.getText())

    def visitMostrar(self, ctx: ExprParser.MostrarContext):
        expr = self.visit(ctx.expr())
        return ASTNode("Mostrar", children=[expr])

    def visitExpr(self, ctx: ExprParser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        left = self.visit(ctx.getChild(0))
        operator = ctx.getChild(1).getText()
        right = self.visit(ctx.getChild(2))
        return ASTNode("Expr", children=[left, right], value=operator)

    def visitTerm(self, ctx: ExprParser.TermContext):
        return ASTNode("Term", children=[self.visit(child) for child in ctx.children])

    def visitFactor(self, ctx: ExprParser.FactorContext):
        if ctx.NUMERO():
            return ASTNode("Literal", value=int(ctx.NUMERO().getText()))
        elif ctx.VARIABLE():
            return ASTNode("Variable", value=ctx.VARIABLE().getText())
        elif ctx.PARENTESIS_INICIAL():
            return self.visit(ctx.expr())

    def visitActualizacion(self, ctx: ExprParser.ActualizacionContext):
        return ASTNode("Actualizacion", children=[self.visit(child) for child in ctx.children])

# Función para generar el AST
def generar_ast(parse_tree):
    visitor = ASTVisitor()
    return visitor.visit(parse_tree)
