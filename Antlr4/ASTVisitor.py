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
    def __init__(self):
        self.current_scope = None
    def visitGramatica(self, ctx: ExprParser.GramaticaContext):
        if not ctx:
            return None
        children = []
        for child in ctx.children:
            visited = self.visit(child)
            if visited is not None:  # Filtrar nodos None
                children.append(visited)
        return ASTNode("Gramatica", children=children)

    def visitPrograma(self, ctx: ExprParser.ProgramaContext):
        if not ctx:
            return None
        children = []
        for child in ctx.children:
            visited = self.visit(child)
            if visited is not None:
                children.append(visited)
        return ASTNode("Programa", children=children)


    def visitBloque(self, ctx: ExprParser.BloqueContext):
        if not ctx:
            return None
        children = []
        for child in ctx.children:
            visited = self.visit(child)
            if visited is not None:
                children.append(visited)
        return ASTNode("Bloque", children=children)

    def visitSentencia(self, ctx: ExprParser.SentenciaContext):
        if not ctx:
            return None
        children = []
        for child in ctx.children:
            visited = self.visit(child)
            if visited is not None:
                children.append(visited)
        return ASTNode("Sentencia", children=children)

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

    def visitDeclaracion(self, ctx: ExprParser.DeclaracionContext):
        if not ctx:
            return None
            
        tipo_node = self.visit(ctx.tipo()) if ctx.tipo() else None
        if not tipo_node:
            return None
            
        nombre = ctx.VARIABLE().getText() if ctx.VARIABLE() else None
        if not nombre:
            return None
            
        valor_node = self.visit(ctx.expr()) if ctx.expr() else None
        
        # Manejar cadenas vacías
        if valor_node is None and tipo_node.value == 'cadena':
            valor_node = ASTNode("Literal", value="")
            
        return ASTNode("Declaracion", 
                     children=[tipo_node, valor_node] if valor_node is not None else [tipo_node],
                     value=nombre)

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
        if not ctx:
            return None
            
        tipo = ctx.getText()
        if not tipo:
            return None
            
        return ASTNode("Tipo", value=tipo)

    def visitMostrar(self, ctx: ExprParser.MostrarContext):
        if not ctx or not ctx.expr():
            return None
            
        expr_node = self.visit(ctx.expr())
        if not expr_node:
            return None
            
        return ASTNode("Mostrar", children=[expr_node])

    def visitExpr(self, ctx: ExprParser.ExprContext):
        if not ctx:
            return None
            
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
            
        left = self.visit(ctx.getChild(0))
        operator = ctx.getChild(1).getText() if ctx.getChildCount() > 1 else None
        right = self.visit(ctx.getChild(2)) if ctx.getChildCount() > 2 else None
        
        if not left or not operator or not right:
            return None
            
        return ASTNode("Expr", children=[left, right], value=operator)

    def visitTerm(self, ctx: ExprParser.TermContext):
        if not ctx:
            return None
            
        children = []
        for child in ctx.children:
            visited = self.visit(child)
            if visited is not None:
                children.append(visited)
                
        if not children:
            return None
            
        return ASTNode("Term", children=children)

    def visitFactor(self, ctx: ExprParser.FactorContext):
        if not ctx:
            return None
            
        if ctx.NUMERO():
            try:
                value = int(ctx.NUMERO().getText())
                return ASTNode("Literal", value=value)
            except:
                return None
                
        elif ctx.VARIABLE():
            return ASTNode("Variable", value=ctx.VARIABLE().getText())
            
        elif ctx.PARENTESIS_INICIAL() and ctx.expr():
            return self.visit(ctx.expr())
            
        elif ctx.CADENA():
            try:
                cadena = ctx.CADENA().getText()[1:-1]  # Eliminar comillas
                return ASTNode("Literal", value=cadena)
            except:
                return None
                
        return None

    def visitActualizacion(self, ctx: ExprParser.ActualizacionContext):
        if not ctx:
            return None
            
        variable = ctx.VARIABLE().getText() if ctx.VARIABLE() else None
        if not variable:
            return None
            
        operador = ctx.MASMAS().getText() if ctx.MASMAS() else (
                  ctx.MENOSMENOS().getText() if ctx.MENOSMENOS() else None)
        
        return ASTNode("Actualizacion", 
                     children=[ASTNode("Variable", value=variable)],
                     value=operador)

# Función para generar el AST
def generar_ast(parse_tree):
    visitor = ASTVisitor()
    return visitor.visit(parse_tree)
