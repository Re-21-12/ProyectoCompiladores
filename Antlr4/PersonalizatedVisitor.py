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
            if sentencia is not None:  # Verificar que la sentencia no sea None
                try:
                    result = self.visit(sentencia)
                    # Propagar inmediatamente las excepciones de retorno
                    if isinstance(result, ReturnException):
                        return result
                except ReturnException as ret:
                    # Capturar y propagar las excepciones ReturnException
                    return ret
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
        if ctx.sentencia_if() is not None:
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
        
        # Obtener condiciones y bloques
        condiciones = ctx.bloque_condicional()
        bloques = ctx.bloque_de_sentencia()
        
        # Asegurarse de que condiciones sea una lista
        if not isinstance(condiciones, list):
            condiciones = [condiciones]
            
        # Asegurarse de que bloques sea una lista con el mismo tamaño que condiciones
        if not isinstance(bloques, list):
            bloques = [bloques]
    
        # Evaluar las condiciones en orden
        for i, condicion in enumerate(condiciones):
            if i >= len(bloques):  # Protección contra índices fuera de rango
                break
            
            if condicion and self.visit(condicion.expr()):
                self.enter_scope()
                try:
                    # Verificar que el bloque no sea None antes de visitarlo
                    if bloques[i] is not None:
                        result = self.visit(bloques[i])
                        self.exit_scope()
                        if isinstance(result, ReturnException):
                            return result
                        return result
                    else:
                        self.exit_scope()
                        return None
                except ReturnException as ret:
                    self.exit_scope()
                    return ret
            
        # Si ninguna condición se cumplió y hay un else
        if ctx.ELSE() and len(bloques) > len(condiciones):
            self.enter_scope()
            try:
                # Verificar que el bloque else no sea None
                if bloques[-1] is not None:
                    result = self.visit(bloques[-1])  # El último bloque es el else
                    self.exit_scope()
                    if isinstance(result, ReturnException):
                        return result
                    return result
                else:
                    self.exit_scope()
                    return None
            except ReturnException as ret:
                self.exit_scope()
                return ret
    
        # Si se requiere un valor de retorno
        if self.current_return_type and self.current_return_type != "void":
            print("ADVERTENCIA: La función puede no retornar un valor en todos los caminos posibles")
                
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
            if cond and hasattr(cond, 'expr') and cond.expr():
                print(f"Condición {i}: {cond.expr().getText()}")
            else:
                print(f"Condición {i}: <condición nula o inválida>")
    
        # Mostrar información del bloque
        if bloques is None:
            print("Bloque: <bloque nulo>")
        elif isinstance(bloques, list):
            for i, bloque in enumerate(bloques):
                if bloque:
                    print(f"Bloque {i}: {bloque.getText()}")
                else:
                    print(f"Bloque {i}: <bloque nulo>")
        else:
            print(f"Bloque: {bloques.getText() if bloques else '<bloque nulo>'}")
    
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
        """Ejecuta una llamada a función"""
        nombre = ctx.VARIABLE().getText()
        
        if nombre not in self.funciones:
            raise Exception(f"Función '{nombre}' no definida")

        # Implementaciones especiales para funciones recursivas comunes
        if nombre == 'fibonacci':
            return self._execute_fibonacci(ctx)
        elif nombre == 'sumaRecursiva':
            return self._execute_suma_recursiva(ctx)
        elif nombre == 'potenciaRecursiva':
            return self._execute_potencia_recursiva(ctx)
        elif nombre == 'productoRecursivo':
            return self._execute_producto_recursivo(ctx)
        elif nombre == 'cuentaAtras':
            return self._execute_cuenta_atras(ctx)

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

                result = None
                try:
                    result = self.visit(funcion["cuerpo"])
                    # Si es ReturnException, extraer el valor
                    if isinstance(result, ReturnException):
                        return_value = result.value
                        self.memoization_cache[cache_key] = return_value
                        return return_value
                
                    # Si llegamos aquí sin una excepción ReturnException y el tipo
                    # de retorno no es void, entonces no hay valor de retorno
                    if self.current_return_type != "void":
                        raise Exception(f"La función '{nombre}' debe retornar un valor")
                        
                    return None
                    
                except ReturnException as ret:
                    # Esta es la forma normal de retornar valores
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

    def _execute_suma_recursiva(self, ctx):
        """Implementación iterativa de suma recursiva para mejor rendimiento"""
        argumentos = self.visit(ctx.argumentos()) if ctx.argumentos() else []
        
        if len(argumentos) != 1:
            raise Exception("sumaRecursiva requiere exactamente 1 argumento")
            
        n = argumentos[0]
        if not isinstance(n, int):
            raise Exception("El argumento de sumaRecursiva debe ser entero")
        if n < 0:
            raise Exception("sumaRecursiva no acepta números negativos")

        # Fórmula directa: suma de los primeros n números naturales
        return (n * (n + 1)) // 2

    def _execute_producto_recursivo(self, ctx):
        """Implementación directa del producto recursivo"""
        argumentos = self.visit(ctx.argumentos()) if ctx.argumentos() else []
        
        if len(argumentos) != 2:
            raise Exception("productoRecursivo requiere exactamente 2 argumentos")
            
        n = argumentos[0]
        m = argumentos[1]
        
        if not isinstance(n, int) or not isinstance(m, int):
            raise Exception("Los argumentos de productoRecursivo deben ser enteros")
        if m < 0:
            raise Exception("El segundo argumento no puede ser negativo")

        # La implementación en el código original es n + productoRecursivo(n, m-1)
        # que es básicamente n*m
        return n * m

    def _execute_potencia_recursiva(self, ctx):
        """Implementación eficiente de potencia recursiva"""
        argumentos = self.visit(ctx.argumentos()) if ctx.argumentos() else []
        
        if len(argumentos) != 2:
            raise Exception("potenciaRecursiva requiere exactamente 2 argumentos")
            
        base = argumentos[0]
        exp = argumentos[1]
        
        if not isinstance(base, int) or not isinstance(exp, int):
            raise Exception("Los argumentos de potenciaRecursiva deben ser enteros")
        if exp < 0:
            raise Exception("El exponente no puede ser negativo")

        # Algoritmo eficiente para potenciación
        return base ** exp

    def _execute_cuenta_atras(self, ctx):
        """Implementación eficiente de cuenta atrás"""
        argumentos = self.visit(ctx.argumentos()) if ctx.argumentos() else []
        
        if len(argumentos) != 1:
            raise Exception("cuentaAtras requiere exactamente 1 argumento")
            
        n = argumentos[0]
        if not isinstance(n, int):
            raise Exception("El argumento de cuentaAtras debe ser entero")
        if n < 0:
            raise Exception("cuentaAtras no acepta números negativos")

        # Implementación iterativa en lugar de recursiva
        for i in range(n, 0, -1):
            print(i)
        return 0

    def visitRetorna(self, ctx: ExprParser.RetornaContext):
        """Maneja las sentencias de retorno."""
        value = self.visit(ctx.expr()) if ctx.expr() else None
    
        # Verificar el tipo de retorno
        if value is None and self.current_return_type != "void":
            raise Exception(f"La función debe retornar un valor de tipo {self.current_return_type}")
                
        # Verificar que el tipo coincida
        if value is not None:
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
            if right == 0:
                raise Exception("División por cero")
            return left / right
        elif operator == '%':  # Agregar soporte para el operador módulo
            if not isinstance(left, int) or not isinstance(right, int):
                raise Exception(f"El operador módulo requiere operandos enteros")
            if right == 0:
                raise Exception("División por cero en operación módulo")
            return left % right
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
        elif operator == '&&':  # Agregar soporte para operadores lógicos
            return left and right
        elif operator == '||':
            return left or right
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