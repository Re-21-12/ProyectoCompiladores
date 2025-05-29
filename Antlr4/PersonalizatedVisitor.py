from ExprVisitor import ExprVisitor
from ExprParser import ExprParser
class PersonalizatedVisitor(  ExprVisitor):
    def __init__(self):
        self.ambitos = [{}]  # Stack de ámbitos (inicia con ámbito global)
        self.funciones = {}  # Diccionario de funciones (nombre: info)
        self.return_value = None
        self.should_return = False

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

    def call_function(self, name, args):
        func = self.get_function(name)

        if len(args) != len(func['params']):
            raise ValueError(f"Argumentos incorrectos para '{name}'. Esperaba {len(func['params'])}, obtuvo {len(args)}")

        self.enter_scope()

        for (param_name, _), arg_value in zip(func['params'], args):
            self.define_variable(param_name, arg_value)

        result = None
        try:
            for stmt in func['body']:
                result = self.visit(stmt)
        except ReturnException as ret:
            result = ret.value

        self.exit_scope()
        return result
    
    def define_function(self, name, params, return_type, body):
        info = {
            'params': params,
            'return_type': return_type,
            'body': body
        }
        self.define_function(name, info)

    def get_function(self, name):
        """Obtiene la información de una función."""
        if name not in self.funciones:
            raise Exception(f"Función '{name}' no definida")
        return self.funciones[name]
    def get_function_return_type(self, name):
        """Obtiene el tipo de retorno de una función si está definida."""
        if name not in self.funciones:
            raise Exception(f"Función '{name}' no definida")
        return self.funciones[name]['return_type']
        
    # Visit a parse tree produced by ExprParser#gramatica.
    def visitGramatica(self, ctx:ExprParser.GramaticaContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#programa.
    def visitPrograma(self, ctx: ExprParser.ProgramaContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#bloque.
    def visitBloque(self, ctx: ExprParser.BloqueContext):
        """Execute statements in block, stopping if return encountered"""
        for sentencia in ctx.sentencia():
            self.visit(sentencia)
            if self.should_return:
                break
        return self.return_value if self.should_return else None

    def visitTipo(self, ctx:ExprParser.TipoContext):
        return self.visitChildren(ctx)

    def visitActualizacion(self, ctx: ExprParser.ActualizacionContext):
        var_name = ctx.VARIABLE().getText()

        for scope in reversed(self.ambitos):
            if var_name in scope:
                if not isinstance(scope[var_name], (int, float)):
                    raise TypeError(f"Error: No se puede actualizar la variable '{var_name}' porque no es numérica")

                if ctx.MASMAS():
                    scope[var_name] += 1
                elif ctx.MENOSMENOS():
                    scope[var_name] -= 1
                elif ctx.expr():
                    new_value = self.visit(ctx.expr())
                    scope[var_name] = new_value

                # Imprimir el nuevo valor para depuración
                print(f"Variable '{var_name}' actualizada a: {scope[var_name]}")
                return scope[var_name]

        raise NameError(f"Variable '{var_name}' no definida.")

    # Visit a parse tree produced by ExprParser#sentencia.
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
        elif ctx.sentencia_switch():
            return self.visitSentencia_switch(ctx.sentencia_switch())
        else:
            raise ValueError(f"Sentencia no reconocida: {ctx.getText()}")

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

    # Visit a parse tree produced by ExprParser#funcion_llamada.
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
        return None

    # Visit a parse tree produced by ExprParser#parametros.
    def visitParametros(self, ctx: ExprParser.ParametrosContext):
        """Process function parameters with their types"""
        return [self.visit(param) for param in ctx.parametro()]

    # Visit a parse tree produced by ExprParser#parametro.
    def visitParametro(self, ctx: ExprParser.ParametroContext):
        """Extract parameter name and type"""
        return {
            "nombre": ctx.VARIABLE().getText(),
            "tipo": ctx.tipo().getText()
        }

    # Visit a parse tree produced by ExprParser#argumentos.
    def visitArgumentos(self, ctx: ExprParser.ArgumentosContext):
        """Process function arguments"""
        return [self.visit(expr) for expr in ctx.expr()] if ctx.expr() else []

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


    def visitBloque_de_sentencia(self, ctx: ExprParser.Bloque_de_sentenciaContext):
        if ctx.sentencia():
            return self.visit(ctx.sentencia())
        else:
            return self.visit(ctx.bloque())

    def _evaluate_condition(self, cond_block: ExprParser.Bloque_condicionalContext):
        return self.visit(cond_block.expr())

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
    
    def _execute_block(self, block: ExprParser.Bloque_de_sentenciaContext):
        result = self.visit(block)
        return result if self.should_return else None
    
    def visitBloque_condicional(self, ctx:ExprParser.Bloque_condicionalContext):
        """Evalúa una condición y ejecuta el bloque si es verdadera."""
        condicion = self.visit(ctx.expr())
        if condicion:
            self.enter_scope()
            resultado = self.visit(ctx.bloque_de_sentencia())
            self.exit_scope()
            return resultado
        return None

    def visitDeclaracion(self, ctx: ExprParser.DeclaracionContext):
        var_name = ctx.VARIABLE().getText()
        var_type = ctx.tipo().getText()

        value = None
        if ctx.expr():
            value = self.visit(ctx.expr())

        self.define_variable(var_name, value)
        return value

    def visitReasignacion(self, ctx: ExprParser.ReasignacionContext):
        var_name = ctx.VARIABLE().getText()
        new_value = self.visit(ctx.expr())

        for scope in reversed(self.ambitos):
            if var_name in scope:
                scope[var_name] = new_value
                print(f"Variable '{var_name}' actualizada a: {new_value}")
                return new_value

        raise NameError(f"Variable '{var_name}' no definida.")

    def visitFuncion_llamada_expr(self, ctx: ExprParser.Funcion_llamada_exprContext):
        """Handle function calls within expressions"""
        return self._execute_function_call(ctx)

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


    def visitRetorna(self, ctx: ExprParser.RetornaContext):
        """Handle return statements, setting the return value and flag"""
        self.return_value = self.visit(ctx.expr())
        self.should_return = True
        return self.return_value

    def visitDeclaracion_sin_asignacion(self, ctx: ExprParser.Declaracion_sin_asignacionContext):
        var_name = ctx.VARIABLE().getText()
        var_type = ctx.tipo().getText()
        self.define_variable(var_name, None)
        return None

    # Visit a parse tree produced by ExprParser#mostrar.

    def visitMostrar(self, ctx: ExprParser.MostrarContext):
        value = self.visit(ctx.expr())
        print(value)


    def visitExpr(self, ctx: ExprParser.ExprContext):
        if ctx.getChildCount() == 1:
            # Caso base: un solo término o factor
            return self.visit(ctx.getChild(0))

        left = self.visit(ctx.getChild(0))
        operator = ctx.getChild(1).getText()
        right = self.visit(ctx.getChild(2))

        if operator == '+':
            return left + right
        elif operator == '-':
            return left - right
        elif operator == '*':
            return left * right
        elif operator == '/':
            return left / right
        elif operator == '<':
            return left < right
        elif operator == '>':
            return left > right
        elif operator == '<=':
            return left <= right
        elif operator == '>=':
            return left >= right
        elif operator == '==':
            return left == right
        elif operator == '!=':
            return left != right
        else:
            raise Exception(f"Operador desconocido: {operator}")

    def visitTerm(self, ctx: ExprParser.TermContext):
        if ctx.getChildCount() == 1:
            # Caso base: un solo factor
            return self.visit(ctx.getChild(0))

        left = self.visit(ctx.getChild(0))
        operator = ctx.getChild(1).getText()
        right = self.visit(ctx.getChild(2))

        if operator == '*':
            return left * right
        elif operator == '/':
            return left / right
        elif operator == '^':  # Soporte para potencias
            return left ** right
        else:
            raise Exception(f"Operador desconocido: {operator}")

    def visitFactor(self, ctx: ExprParser.FactorContext):
        if ctx.RAIZ():
            # Soporte para raíces
            value = self.visit(ctx.expr())
            if value < 0:
                raise ValueError("No se puede calcular la raíz de un número negativo")
            return value ** 0.5
        elif ctx.NUMERO():
            return int(ctx.NUMERO().getText())
        elif ctx.DECIMAL():
            return float(ctx.DECIMAL().getText())
        elif ctx.BOOLEANO():
            return ctx.BOOLEANO().getText() == "verdadero"
        elif ctx.CADENA():
            return ctx.CADENA().getText()[1:-1]  # Eliminar comillas
        elif ctx.VARIABLE():
            return self.get_variable(ctx.VARIABLE().getText())
        elif ctx.PARENTESIS_INICIAL():
            return self.visit(ctx.expr())
        elif ctx.MENOS():
            return -self.visit(ctx.factor())
        elif ctx.funcion_llamada_expr():
            return self.visit(ctx.funcion_llamada_expr())
        else:
            raise Exception("Factor desconocido")
        
    def traducir_tipo(self, value):
        print("valor obtenido",value)
        if isinstance(value, bool):
            return "bool"        
        elif isinstance(value, int):
            return "entero"
        elif isinstance(value, float):
            return "decimal"
        elif isinstance(value, str):
            return "cadena"

        return "desconocido"

    def visitSentencia_switch(self, ctx: ExprParser.Sentencia_switchContext):
        """Maneja la sentencia switch."""
        switch_value = self.visit(ctx.expr())  # Evaluar la expresión del switch
        matched = False

        # Procesar los casos
        for case in ctx.getChildren():
            if case.getText().startswith("case"):
                case_value = self.visit(case.expr())
                if switch_value == case_value:
                    self.enter_scope()
                    self.visit(case.bloque())
                    self.exit_scope()
                    matched = True
                    break

        # Procesar el caso default si no hubo coincidencias
        if not matched and ctx.getChild(ctx.getChildCount() - 2).getText() == "default":
            self.enter_scope()
            self.visit(ctx.bloque(ctx.getChildCount() - 1))
            self.exit_scope()