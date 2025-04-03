from ExprVisitor import ExprVisitor
class ASTNode:
    def __init__(self, node_type, children=None, value=None, line=None, column=None):
        self.type = node_type
        self.children = children if children is not None else []
        self.value = value
        self.line = line
        self.column = column

    def __repr__(self, level=0):
        ret = "  " * level + f"{self.type}"
        if self.value is not None:
            ret += f": {self.value}"
        ret += "\n"
        for child in self.children:
            if isinstance(child, ASTNode):
                ret += child.__repr__(level + 1)
            else:
                ret += "  " * (level + 1) + f"{child}\n"
        return ret

class ASTVisitor(ExprVisitor):
    def __init__(self):
        super().__init__()
        self.current_scope = None
    
    def visitGramatica(self, ctx):
        program = self.visit(ctx.programa())
        return ASTNode('Program', children=[program])
    
    def visitPrograma(self, ctx):
        block = self.visit(ctx.bloque())
        return ASTNode('MainFunction', children=[block])
    
    def visitBloque(self, ctx):
        statements = [self.visit(child) for child in ctx.sentencia()]
        return ASTNode('Block', children=statements)
    
    def visitSentencia(self, ctx):
        # Get the first non-null child (declaration, if, while, etc.)
        return self.visit(ctx.getChild(0))
    
    def visitSentencia_if(self, ctx):
        if_blocks = []
        conditions = []
        
        # Process all if/else if blocks
        for cond_block in ctx.bloque_condicional():
            condition = self.visit(cond_block.expr())
            block = self.visit(cond_block.bloque_de_sentencia())
            conditions.append(condition)
            if_blocks.append(block)
        
        # Process else block if exists
        else_block = None
        if ctx.ELSE():
            else_block = self.visit(ctx.bloque_de_sentencia())
        
        return ASTNode('IfStatement', 
                     children=[ASTNode('Conditions', children=conditions),
                               ASTNode('IfBlocks', children=if_blocks),
                               else_block] if else_block else 
                               [ASTNode('Conditions', children=conditions),
                                ASTNode('IfBlocks', children=if_blocks)])
    
    def visitSentencia_while(self, ctx):
        condition = self.visit(ctx.expr())
        body = self.visit(ctx.bloque_de_sentencia())
        return ASTNode('WhileLoop', children=[condition, body])
    
    def visitSentencia_for(self, ctx):
        init = self.visit(ctx.declaracion())
        condition = self.visit(ctx.expr())
        update = self.visit(ctx.actualizacion())
        body = self.visit(ctx.bloque_de_sentencia())
        return ASTNode('ForLoop', children=[init, condition, update, body])
    
    def visitDeclaracion_funcion(self, ctx):
        name = ctx.VARIABLE().getText()
        return_type = self.visit(ctx.tipo())
        
        # Process parameters
        params = []
        if ctx.parametros():
            params = [self.visit(param) for param in ctx.parametros().parametro()]
        
        body = self.visit(ctx.bloque())
        return_expr = self.visit(ctx.expr())
        
        return ASTNode('FunctionDecl',
                      children=[return_type, 
                                ASTNode('Parameters', children=params),
                                body,
                                return_expr],
                      value=name)
    
    def visitFuncion_llamada(self, ctx):
        name = ctx.VARIABLE().getText()
        args = []
        if ctx.argumentos():
            args = [self.visit(arg) for arg in ctx.argumentos().expr()]
        return ASTNode('FunctionCall', children=args, value=name)
    
    def visitParametro(self, ctx):
        name = ctx.VARIABLE().getText()
        param_type = self.visit(ctx.tipo())
        return ASTNode('Parameter', children=[param_type], value=name)
    
    def visitBloque_condicional(self, ctx):
        # This is handled directly in visitSentencia_if
        pass
    
    def visitBloque_de_sentencia(self, ctx):
        if ctx.sentencia():
            return self.visit(ctx.sentencia())
        else:
            return self.visit(ctx.bloque())
    
    def visitDeclaracion(self, ctx):
        var_name = ctx.VARIABLE().getText()
        var_type = self.visit(ctx.tipo())
        value = self.visit(ctx.expr())
        return ASTNode('VariableDecl', children=[var_type, value], value=var_name)
    
    def visitReasignacion(self, ctx):
        var_name = ctx.VARIABLE().getText()
        value = self.visit(ctx.expr())
        return ASTNode('Assignment', children=[value], value=var_name)
    
    def visitTipo(self, ctx):
        return ASTNode('Type', value=ctx.getText())
    
    def visitMostrar(self, ctx):
        expr = self.visit(ctx.expr())
        return ASTNode('PrintStatement', children=[expr])
    
    def visitExpr(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.term(0))
        
        # Handle comparisons
        if ctx.MENOR_QUE() or ctx.MAYOR_QUE() or ctx.MENOR_IGUAL_QUE() or ctx.MAYOR_IGUAL_QUE() or ctx.IGUAL() or ctx.DIFERENTE():
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            op = ctx.getChild(1).getText()
            return ASTNode('BinaryOp', children=[left, right], value=op)
        
        # Handle addition/subtraction
        if ctx.MAS() or ctx.MENOS():
            left = self.visit(ctx.term(0))
            right = self.visit(ctx.term(1))
            op = ctx.getChild(1).getText()
            return ASTNode('BinaryOp', children=[left, right], value=op)
        
        return None
    
    def visitTerm(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.factor(0))
        
        # Handle multiplication/division
        if ctx.MULTIPLICACION() or ctx.DIVISION():
            left = self.visit(ctx.factor(0))
            right = self.visit(ctx.factor(1))
            op = ctx.getChild(1).getText()
            return ASTNode('BinaryOp', children=[left, right], value=op)
        
        return None
    
    def visitFactor(self, ctx):
        if ctx.NUMERO():
            return ASTNode('Literal', value=int(ctx.NUMERO().getText()))
        elif ctx.DECIMAL():
            return ASTNode('Literal', value=float(ctx.DECIMAL().getText()))
        elif ctx.BOOLEANO():
            return ASTNode('Literal', value=ctx.BOOLEANO().getText() == "verdadero")
        elif ctx.CADENA():
            return ASTNode('Literal', value=ctx.CADENA().getText()[1:-1])  # Remove quotes
        elif ctx.VARIABLE():
            return ASTNode('Variable', value=ctx.VARIABLE().getText())
        elif ctx.PARENTESIS_INICIAL() and ctx.expr():
            return self.visit(ctx.expr())
        elif ctx.MENOS() and ctx.factor():
            operand = self.visit(ctx.factor())
            return ASTNode('UnaryOp', children=[operand], value="-")
        elif ctx.VARIABLE() and (ctx.MASMAS() or ctx.MENOSMENOS()):
            op = ctx.getChild(1).getText()
            return ASTNode('UnaryOp', 
                         children=[ASTNode('Variable', value=ctx.VARIABLE().getText())],
                         value=op)
        return None
    
    def visitActualizacion(self, ctx):
        var_name = ctx.VARIABLE().getText()
        
        if ctx.MASMAS() or ctx.MENOSMENOS():
            op = ctx.getChild(1).getText()
            return ASTNode('UnaryOp',
                         children=[ASTNode('Variable', value=var_name)],
                         value=op)
        elif ctx.expr():
            expr = self.visit(ctx.expr())
            return ASTNode('Assignment',
                          children=[expr],
                          value=var_name)
        return None