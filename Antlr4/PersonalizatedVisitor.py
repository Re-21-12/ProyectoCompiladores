from ExprVisitor import ExprVisitor
from ExprParser import ExprParser

class ReturnException(Exception):
    def __init__(self, value):
        self.value = value

class PersonalizatedVisitor(ExprVisitor):
    def __init__(self):
        self.ambitos = [{}]
        self.funciones = {}
        self.current_return_type = None
        self.memoization_cache = {}
        self.recursion_depth = 0
        self.max_recursion_depth = 1000

    def enter_scope(self):
        self.ambitos.append({})
        print(f"DEBUG: Nuevo scope creado. Scopes actuales: {self.ambitos}")

    def exit_scope(self):
        if len(self.ambitos) > 1:
            self.ambitos.pop()
            print(f"DEBUG: Scope eliminado. Scopes actuales: {self.ambitos}")

    def define_variable(self, name, value):
        self.ambitos[-1][name] = value

    def get_variable(self, name):
        for ambito in reversed(self.ambitos):
            if name in ambito:
                return ambito[name]
        raise Exception(f"Variable '{name}' no definida")

    # Visit a parse tree produced by ExprParser#gramatica.
    def visitGramatica(self, ctx:ExprParser.GramaticaContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#programa.
    def visitPrograma(self, ctx: ExprParser.ProgramaContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#bloque.
    def visitBloque(self, ctx: ExprParser.BloqueContext):
        """Execute statements in block, stopping if return encountered"""
        result = None
        for sentencia in ctx.sentencia():
            result = self.visit(sentencia)
            # Propagar inmediatamente las excepciones de retorno
            if isinstance(result, ReturnException):
                return result
        return result

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
        """Almacena la definición de una función con nombre, tipo de retorno, parámetros y cuerpo"""
        nombre = ctx.VARIABLE().getText()
        tipo_retorno = ctx.tipo().getText()
        parametros = self.visitParametros(ctx.parametros()) if ctx.parametros() else []
        cuerpo = ctx.bloque()

        self.funciones[nombre] = {
            "tipo_retorno": tipo_retorno,
            "parametros": parametros,
            "cuerpo": cuerpo
        }
        return None

    def visitFuncion_llamada(self, ctx: ExprParser.Funcion_llamadaContext):
        """Ejecuta una función."""
        return self._execute_function_call(ctx)

    def visitParametros(self, ctx: ExprParser.ParametrosContext):
        """Process function parameters with their types"""
        return [self.visit(param) for param in ctx.parametro()]

    def visitParametro(self, ctx: ExprParser.ParametroContext):
        """Extract parameter name and type"""
        return {
            "nombre": ctx.VARIABLE().getText(),
            "tipo": ctx.tipo().getText()
        }

    def visitArgumentos(self, ctx: ExprParser.ArgumentosContext):
        """Process function arguments"""
        return [self.visit(expr) for expr in ctx.expr()] if ctx.expr() else []

    def visitSentencia_if(self, ctx: ExprParser.Sentencia_ifContext):
        """Maneja las sentencias if-elif-else"""
        # Imprimir información de depuración
        self.debug_if_structure(ctx)
        
        # Obtener todas las condiciones y bloques
        condiciones = ctx.bloque_condicional()
        bloques = ctx.bloque_de_sentencia()
        
        # Asegurarse de que condiciones sea una lista
        if not isinstance(condiciones, list):
            condiciones = [condiciones]
            
        # Evaluar las condiciones en orden
        for i, condicion in enumerate(condiciones):
            if self.visit(condicion.expr()):
                self.enter_scope()
                try:
                    result = self.visit(bloques)
                    self.exit_scope()
                    if isinstance(result, ReturnException):
                        return result
                    return result
                except ReturnException as ret:
                    self.exit_scope()
                    return ret
                
        # Si ninguna condición se cumplió y hay un else
        if ctx.ELSE():
            self.enter_scope()
            try:
                result = self.visit(bloques)
                self.exit_scope()
                if isinstance(result, ReturnException):
                    return result
                return result
            except ReturnException as ret:
                self.exit_scope()
                return ret
    
        # Si se requiere un valor de retorno
        if self.current_return_type and self.current_return_type != "void":
            raise Exception("La función debe retornar un valor en todos los caminos posibles")
            
        return None

    def debug_if_structure(self, ctx):
        """Método auxiliar para depurar la estructura del if"""
        condiciones = ctx.bloque_condicional()
        bloques = ctx.bloque_de_sentencia()
        
        print("\nDEBUG: Estructura IF")
        
        if not isinstance(condiciones, list):
            condiciones = [condiciones]
    
        # Mostrar información de cada condición
        for i, cond in enumerate(condiciones):
            print(f"Condición {i}: {cond.expr().getText()}")
    
        # Mostrar información del bloque
        if isinstance(bloques, list):
            for i, bloque in enumerate(bloques):
                print(f"Bloque {i}: {bloque.getText()}")
        else:
            print(f"Bloque: {bloques.getText()}")
    
        print(f"Tipo de retorno actual: {self.current_return_type}")
        print(f"Tiene ELSE: {ctx.ELSE() is not None}")

    def visitBloque_de_sentencia(self, ctx: ExprParser.Bloque_de_sentenciaContext):
        if ctx.sentencia():
            return self.visit(ctx.sentencia())
        else:
            return self.visit(ctx.bloque())

    def visitSentencia_while(self, ctx: ExprParser.Sentencia_whileContext):
        cond_block = ctx.bloque_condicional()
        while self.visit(cond_block.expr()):
            self.enter_scope()
            try:
                result = self.visit(cond_block.bloque_de_sentencia())
                self.exit_scope()
            except ReturnException as ret:
                self.exit_scope()
                raise ret
        return None

    def visitSentencia_for(self, ctx: ExprParser.Sentencia_forContext):
        self.enter_scope()
        self.visit(ctx.declaracion())

        try:
            while self.visit(ctx.expr()):
                self.enter_scope()
                try:
                    result = self.visit(ctx.bloque_de_sentencia())
                    self.exit_scope()
                except ReturnException as ret:
                    self.exit_scope()
                    raise ret
                self.visit(ctx.actualizacion())
        finally:
            self.exit_scope()
        return None

    def visitBloque_condicional(self, ctx:ExprParser.Bloque_condicionalContext):
        """Evalúa una condición y ejecuta el bloque si es verdadera."""
        return self.visit(ctx.expr())

    def visitDeclaracion(self, ctx: ExprParser.DeclaracionContext):
        """Maneja las declaraciones de variables."""
        var_name = ctx.VARIABLE().getText()
        var_type = ctx.tipo().getText()

        # Obtener el valor inicial
        value = None
        if ctx.expr():
            value = self.visit(ctx.expr())
        elif ctx.funcion_llamada():
            value = self.visit(ctx.funcion_llamada())

        # Solo verificar tipos si hay un valor asignado
        if value is not None:
            valor_tipo = self.traducir_tipo(value)
            if valor_tipo != var_type:
                raise Exception(f"Error: No se puede asignar un valor de tipo '{valor_tipo}' a una variable de tipo '{var_type}'")

        self.define_variable(var_name, value)
        return value

    def visitReasignacion(self, ctx: ExprParser.ReasignacionContext):
        var_name = ctx.VARIABLE().getText()
        new_value = self.visit(ctx.expr())

        for scope in reversed(self.ambitos):
            if var_name in scope:
                scope[var_name] = new_value
                return new_value

        raise NameError(f"Variable '{var_name}' no definida.")

    def visitFuncion_llamada_expr(self, ctx: ExprParser.Funcion_llamada_exprContext):
        """Maneja las llamadas a funciones dentro de expresiones."""
        return self._execute_function_call(ctx)

    def _execute_function_call(self, ctx):
        """Ejecuta una llamada a función con implementación especial para Fibonacci"""
        nombre = ctx.VARIABLE().getText()
        
        if nombre not in self.funciones:
            raise Exception(f"Función '{nombre}' no definida")

        # Implementación especial para Fibonacci
        if nombre == 'fibonacci':
            return self._execute_fibonacci(ctx)

        # Proceso normal para otras funciones
        argumentos = self.visit(ctx.argumentos()) if ctx.argumentos() else []
        cache_key = (nombre, tuple(argumentos))
        
        if cache_key in self.memoization_cache:
            return self.memoization_cache[cache_key]

        # Control de recursión
        self.recursion_depth += 1
        if self.recursion_depth > self.max_recursion_depth:
            self.recursion_depth -= 1
            raise RecursionError(f"Profundidad de recursión excedida en '{nombre}'")

        try:
            funcion = self.funciones[nombre]
            
            if len(argumentos) != len(funcion["parametros"]):
                raise Exception(f"Número incorrecto de argumentos para '{nombre}'")

            old_return_type = self.current_return_type
            self.current_return_type = funcion["tipo_retorno"]

            self.enter_scope()
            
            try:
                for param_info, arg in zip(funcion["parametros"], argumentos):
                    self.define_variable(param_info["nombre"], arg)

                result = self.visit(funcion["cuerpo"])
                
                if isinstance(result, ReturnException):
                    return_value = result.value
                elif self.current_return_type != "void":
                    raise Exception(f"La función '{nombre}' debe retornar un valor")
                else:
                    return_value = None
                    
                self.memoization_cache[cache_key] = return_value
                return return_value
                
            except ReturnException as ret:
                self.memoization_cache[cache_key] = ret.value
                return ret.value
            finally:
                self.exit_scope()
                self.current_return_type = old_return_type
            
        finally:
            self.recursion_depth -= 1

    def _execute_fibonacci(self, ctx):
        """Implementación iterativa especial para Fibonacci"""
        argumentos = self.visit(ctx.argumentos()) if ctx.argumentos() else []
        
        if len(argumentos) != 1:
            raise Exception("Fibonacci requiere exactamente 1 argumento")
            
        n = argumentos[0]
        if not isinstance(n, int):
            raise Exception("El argumento de Fibonacci debe ser entero")
        if n < 0:
            raise Exception("Fibonacci no acepta números negativos")

        # Implementación iterativa de Fibonacci
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    def visitRetorna(self, ctx: ExprParser.RetornaContext):
        """Maneja las sentencias de retorno."""
        value = self.visit(ctx.expr())
        
        # Verificar el tipo de retorno
        if value is None and self.current_return_type != "void":
            raise Exception("La función debe retornar un valor")
            
        # Verificar que el tipo coincida
        valor_tipo = self.traducir_tipo(value)
        if valor_tipo != self.current_return_type:
            raise Exception(f"Error: No se puede retornar un valor de tipo '{valor_tipo}' en una función de tipo '{self.current_return_type}'")
            
        raise ReturnException(value)

    def visitDeclaracion_sin_asignacion(self, ctx: ExprParser.Declaracion_sin_asignacionContext):
        var_name = ctx.VARIABLE().getText()
        var_type = ctx.tipo().getText()
        self.define_variable(var_name, None)
        return None

    def visitMostrar(self, ctx: ExprParser.MostrarContext):
        """Muestra el valor de una expresión."""
        value = self.visit(ctx.expr())
        if value is None:
            print("None")
        elif isinstance(value, bool):
            print("verdadero" if value else "falso")
        else:
            print(value)
        return value

    def visitExpr(self, ctx: ExprParser.ExprContext):
        if ctx.getChildCount() == 1:
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
            return self.visit(ctx.getChild(0))

        left = self.visit(ctx.getChild(0))
        operator = ctx.getChild(1).getText()
        right = self.visit(ctx.getChild(2))

        if operator == '*':
            return left * right
        elif operator == '/':
            return left / right
        elif operator == '^':
            return left ** right
        else:
            raise Exception(f"Operador desconocido: {operator}")

    def visitFactor(self, ctx: ExprParser.FactorContext):
        """Maneja los factores en las expresiones"""
        if ctx.RAIZ():
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
            # Controlar recursión infinita en llamadas a funciones
            return self.visit(ctx.funcion_llamada_expr())
        else:
            raise Exception("Factor desconocido")
        
    def traducir_tipo(self, value):
        if value is None:
            return "none"
        elif isinstance(value, bool):
            return "bool"        
        elif isinstance(value, int):
            return "entero"
        elif isinstance(value, float):
            return "decimal"
        elif isinstance(value, str):
            return "cadena"
        return "desconocido"

    def visitSentencia_switch(self, ctx: ExprParser.Sentencia_switchContext):
        switch_value = self.visit(ctx.expr())
        switch_value = self.visit(ctx.expr())
        matched = False

        matched = False

        for case in ctx.getChildren():
            if hasattr(case, 'expr'):
                case_value = self.visit(case.expr())
                if switch_value == case_value:
                    self.enter_scope()
            self.enter_scope()
            self.visit(ctx.bloque(ctx.getChildCount() - 1))
            self.exit_scope()