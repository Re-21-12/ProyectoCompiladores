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
        return self.visit(ctx.getChild(0))
    
    def visitSentencia_if(self, ctx):
        conditions = []
        blocks = []
        
        # Procesar los bloques condicionales
        if ctx.bloque_condicional():
            for cond_block in ctx.bloque_condicional():
                # Verifica que el bloque de sentencia exista antes de visitarlo
                bloque_sentencia = cond_block.bloque_de_sentencia()
                if bloque_sentencia is not None:
                    blocks.append(self.visit(bloque_sentencia))
                else:
                    blocks.append(ASTNode('Empty'))
                conditions.append(self.visit(cond_block.expr()))
        
        # Procesar else si existe
        else_block = None
        if ctx.ELSE():
            bloque_else = ctx.bloque_de_sentencia()
            if bloque_else is not None:
                else_block = self.visit(bloque_else)
            else:
                else_block = ASTNode('Empty')
        
        nodes = [
            ASTNode('Conditions', children=conditions),
            ASTNode('Blocks', children=blocks)
        ]
        if else_block:
            nodes.append(else_block)
        
        return ASTNode('IfStatement', children=nodes)
        
    def visitSentencia_while(self, ctx):
        cond_block = ctx.bloque_condicional()
        condition = self.visit(cond_block.expr())
        body = self.visit(cond_block.bloque_de_sentencia())
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

        params = []
        if ctx.parametros():
            params = [self.visit(param) for param in ctx.parametros().parametro()]

        body = self.visit(ctx.bloque()) if ctx.bloque() else None

        return_expr = None
        if ctx.retorna() is not None and ctx.retorna().expr() is not None:
            return_expr = self.visit(ctx.retorna().expr())

        children = [return_type, ASTNode('Parameters', children=params)]
        if body:
            children.append(body)
        if return_expr:
            children.append(ASTNode('ReturnStatement', children=[return_expr]))

        return ASTNode('FunctionDecl', children=children, value=name)
    
    def visitFuncion_llamada(self, ctx):
        name = ctx.VARIABLE().getText()
        args = []
        if ctx.argumentos():
            args = [self.visit(arg) for arg in ctx.argumentos().expr()]
        return ASTNode('FunctionCall', children=args, value=name)
    
    def visitFuncion_llamada_expr(self, ctx):
        return self.visitFuncion_llamada(ctx)
    
    def visitRetorna(self, ctx):
        expr = self.visit(ctx.expr())
        return ASTNode('ReturnStatement', children=[expr])
    
    def visitParametro(self, ctx):
        name = ctx.VARIABLE().getText()
        param_type = self.visit(ctx.tipo())
        return ASTNode('Parameter', children=[param_type], value=name)
    
    def visitBloque(self, ctx):
        statements = []
        for child in ctx.sentencia():
            if child is not None:
                result = self.visit(child)
                if result is not None:
                    statements.append(result)
        return ASTNode('Block', children=statements)

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
    
    def visitDeclaracion_sin_asignacion(self, ctx):
        var_name = ctx.VARIABLE().getText()
        var_type = self.visit(ctx.tipo())
        return ASTNode('VariableDecl', children=[var_type], value=var_name)
    
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
        # Handle comparison operations
        if ctx.getChildCount() == 3 and (
            ctx.MENOR_QUE() or ctx.MAYOR_QUE() or 
            ctx.MENOR_IGUAL_QUE() or ctx.MAYOR_IGUAL_QUE() or 
            ctx.IGUAL() or ctx.DIFERENTE()
        ):
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            op = ctx.getChild(1).getText()
            return ASTNode('BinaryOp', children=[left, right], value=op)
        
        # Handle addition/subtraction
        if ctx.getChildCount() >= 3 and (ctx.MAS() or ctx.MENOS()):
            left = self.visit(ctx.term(0))
            right = self.visit(ctx.term(1))
            op = ctx.getChild(1).getText()
            return ASTNode('BinaryOp', children=[left, right], value=op)
        
        # Handle single term
        return self.visit(ctx.term(0))
    
    def visitTerm(self, ctx):
        # Handle multiplication/division
        if ctx.getChildCount() >= 3 and (ctx.MULTIPLICACION() or ctx.DIVISION()):
            left = self.visit(ctx.factor(0))
            right = self.visit(ctx.factor(1))
            op = ctx.getChild(1).getText()
            return ASTNode('BinaryOp', children=[left, right], value=op)
        
        # Handle single factor
        return self.visit(ctx.factor(0))
    
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
        elif ctx.funcion_llamada_expr():
            return self.visit(ctx.funcion_llamada_expr())
        elif ctx.expr():
            return self.visit(ctx.expr())
        elif ctx.MENOS() and ctx.factor():
            operand = self.visit(ctx.factor())
            return ASTNode('UnaryOp', children=[operand], value="-")
        elif ctx.VARIABLE() and (ctx.MASMAS() or ctx.MENOSMENOS()):
            op = ctx.getChild(1).getText()
            return ASTNode('UnaryOp', 
                         children=[ASTNode('Variable', value=ctx.VARIABLE().getText())],
                         value=op)
        return ASTNode('Empty')
    
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
        return ASTNode('Empty')