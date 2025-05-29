from ExprVisitor import ExprVisitor
from ExprParser import ExprParser

class PersonalizatedVisitor(ExprVisitor):
    def __init__(self):
        super().__init__()
        self.ambitos = [{}]  # Stack de ámbitos (inicia con ámbito global)
        self.funciones = {}  # Diccionario de funciones (nombre: info)
        self.return_value = None
        self.should_return = False

    # Métodos de manejo de ámbitos
    def enter_scope(self):
        """Crear un nuevo ámbito (nuevo diccionario en la pila)."""
        self.ambitos.append({})

    def exit_scope(self):
        """Eliminar el último ámbito (salir del bloque actual)."""
        if len(self.ambitos) > 1:  # No permitir eliminar el ámbito global
            self.ambitos.pop()

    def define_variable(self, name, value):
        """Define una variable en el ámbito actual."""
        self.ambitos[-1][name] = value

    def get_variable(self, name):
        """Busca la variable en los ámbitos disponibles (de local a global)."""
        for ambito in reversed(self.ambitos):
            if name in ambito:
                return ambito[name]
        raise Exception(f"Variable '{name}' no definida")

    # Métodos relacionados con sentencias
    def visitSentencia_if(self, ctx: ExprParser.Sentencia_ifContext):
        """Maneja sentencias if, else if y else."""
        condiciones = ctx.bloque_condicional()
        bloques = ctx.bloque_de_sentencia()

        if not isinstance(condiciones, list):
            condiciones = [condiciones]
        if not isinstance(bloques, list):
            bloques = [bloques]

        # Main if
        if self.visit(condiciones[0]):
            self.enter_scope()
            result = self.visit(bloques[0])
            self.exit_scope()
            return result

        # Else ifs
        for i in range(1, len(condiciones)):
            if self.visit(condiciones[i]):
                self.enter_scope()
                result = self.visit(bloques[i])
                self.exit_scope()
                return result

        # Else
        if ctx.ELSE():
            self.enter_scope()
            result = self.visit(bloques[-1])
            self.exit_scope()
            return result

        return None

    def visitSentencia_while(self, ctx: ExprParser.Sentencia_whileContext):
        """Maneja ciclos while."""
        while self.visit(ctx.bloque_condicional()):
            self.enter_scope()
            self.visit(ctx.bloque_de_sentencia())
            self.exit_scope()

    def visitSentencia_for(self, ctx: ExprParser.Sentencia_forContext):
        """Maneja ciclos for."""
        self.enter_scope()
        self.visit(ctx.declaracion())  # Declaración inicial
        while self.visit(ctx.expr()):  # Condición
            self.enter_scope()
            self.visit(ctx.bloque_de_sentencia())
            self.exit_scope()
            self.visit(ctx.actualizacion())  # Actualización
        self.exit_scope()

    # Métodos relacionados con expresiones
    def visitExpr(self, ctx: ExprParser.ExprContext):
        """Evalúa expresiones aritméticas y lógicas."""
        if ctx.MENOR_QUE():
            return self.visit(ctx.expr(0)) < self.visit(ctx.expr(1))
        elif ctx.MAYOR_QUE():
            return self.visit(ctx.expr(0)) > self.visit(ctx.expr(1))
        elif ctx.MENOR_IGUAL_QUE():
            return self.visit(ctx.expr(0)) <= self.visit(ctx.expr(1))
        elif ctx.MAYOR_IGUAL_QUE():
            return self.visit(ctx.expr(0)) >= self.visit(ctx.expr(1))
        elif ctx.IGUAL():
            return self.visit(ctx.expr(0)) == self.visit(ctx.expr(1))
        elif ctx.DIFERENTE():
            return self.visit(ctx.expr(0)) != self.visit(ctx.expr(1))
        elif ctx.MAS():
            return self.visit(ctx.term(0)) + self.visit(ctx.term(1))
        elif ctx.MENOS():
            return self.visit(ctx.term(0)) - self.visit(ctx.term(1))
        else:
            return self.visit(ctx.term(0))

    def visitTerm(self, ctx: ExprParser.TermContext):
        """Evalúa términos (multiplicación y división)."""
        if ctx.MULTIPLICACION():
            return self.visit(ctx.factor(0)) * self.visit(ctx.factor(1))
        elif ctx.DIVISION():
            divisor = self.visit(ctx.factor(1))
            if divisor == 0:
                raise ZeroDivisionError("Error: División por cero.")
            return self.visit(ctx.factor(0)) / divisor
        else:
            return self.visit(ctx.factor(0))

    def visitFactor(self, ctx: ExprParser.FactorContext):
        """Evalúa factores (números, variables, expresiones entre paréntesis)."""
        if ctx.NUMERO():
            return int(ctx.NUMERO().getText())
        elif ctx.DECIMAL():
            return float(ctx.DECIMAL().getText())
        elif ctx.BOOLEANO():
            return ctx.BOOLEANO().getText() == "verdadero"
        elif ctx.CADENA():
            return ctx.CADENA().getText()[1:-1]  # Elimina las comillas
        elif ctx.VARIABLE():
            return self.get_variable(ctx.VARIABLE().getText())
        elif ctx.funcion_llamada_expr():
            return self.visit(ctx.funcion_llamada_expr())
        elif ctx.expr():
            return self.visit(ctx.expr())
        elif ctx.MENOS():
            return -self.visit(ctx.factor())
        else:
            raise ValueError("Factor no reconocido.")

    # Métodos relacionados con funciones
    def visitDeclaracion_funcion(self, ctx: ExprParser.Declaracion_funcionContext):
        """Define una función."""
        nombre = ctx.VARIABLE().getText()
        tipo_retorno = ctx.tipo().getText()
        parametros = self.visit(ctx.parametros()) if ctx.parametros() else []
        cuerpo = ctx.bloque()
        retorno = ctx.retorna()

        self.funciones[nombre] = {
            "tipo_retorno": tipo_retorno,
            "parametros": parametros,
            "cuerpo": cuerpo,
            "retorno": retorno
        }

    def visitFuncion_llamada(self, ctx: ExprParser.Funcion_llamadaContext):
        """Ejecuta una función."""
        nombre = ctx.VARIABLE().getText()
        if nombre not in self.funciones:
            raise Exception(f"Función '{nombre}' no definida.")

        funcion = self.funciones[nombre]
        argumentos = self.visit(ctx.argumentos()) if ctx.argumentos() else []

        if len(argumentos) != len(funcion["parametros"]):
            raise Exception(f"Número incorrecto de argumentos para la función '{nombre}'.")

        self.enter_scope()
        for param, arg in zip(funcion["parametros"], argumentos):
            self.define_variable(param["nombre"], arg)

        self.visit(funcion["cuerpo"])
        self.exit_scope()

    def visitRetorna(self, ctx: ExprParser.RetornaContext):
        """Maneja la sentencia de retorno."""
        self.return_value = self.visit(ctx.expr())
        self.should_return = True
        return self.return_value

    # Métodos faltantes de ExprVisitor
    def visitGramatica(self, ctx: ExprParser.GramaticaContext):
        return self.visitChildren(ctx)

    def visitPrograma(self, ctx: ExprParser.ProgramaContext):
        return self.visitChildren(ctx)

    def visitBloque(self, ctx: ExprParser.BloqueContext):
        return self.visitChildren(ctx)

    def visitFuncion_llamada_expr(self, ctx: ExprParser.Funcion_llamada_exprContext):
        return self.visitChildren(ctx)

    def visitParametros(self, ctx: ExprParser.ParametrosContext):
        return self.visitChildren(ctx)

    def visitParametro(self, ctx: ExprParser.ParametroContext):
        return self.visitChildren(ctx)

    def visitArgumentos(self, ctx: ExprParser.ArgumentosContext):
        return self.visitChildren(ctx)

    def visitBloque_condicional(self, ctx: ExprParser.Bloque_condicionalContext):
        return self.visitChildren(ctx)

    def visitTipo(self, ctx: ExprParser.TipoContext):
        return self.visitChildren(ctx)

