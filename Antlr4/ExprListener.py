# Generated from Expr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#gramatica.
    def enterGramatica(self, ctx:ExprParser.GramaticaContext):
        pass

    # Exit a parse tree produced by ExprParser#gramatica.
    def exitGramatica(self, ctx:ExprParser.GramaticaContext):
        pass


    # Enter a parse tree produced by ExprParser#programa.
    def enterPrograma(self, ctx:ExprParser.ProgramaContext):
        pass

    # Exit a parse tree produced by ExprParser#programa.
    def exitPrograma(self, ctx:ExprParser.ProgramaContext):
        pass


    # Enter a parse tree produced by ExprParser#bloque.
    def enterBloque(self, ctx:ExprParser.BloqueContext):
        pass

    # Exit a parse tree produced by ExprParser#bloque.
    def exitBloque(self, ctx:ExprParser.BloqueContext):
        pass


    # Enter a parse tree produced by ExprParser#sentencia.
    def enterSentencia(self, ctx:ExprParser.SentenciaContext):
        pass

    # Exit a parse tree produced by ExprParser#sentencia.
    def exitSentencia(self, ctx:ExprParser.SentenciaContext):
        pass


    # Enter a parse tree produced by ExprParser#sentencia_if.
    def enterSentencia_if(self, ctx:ExprParser.Sentencia_ifContext):
        pass

    # Exit a parse tree produced by ExprParser#sentencia_if.
    def exitSentencia_if(self, ctx:ExprParser.Sentencia_ifContext):
        pass


    # Enter a parse tree produced by ExprParser#sentencia_while.
    def enterSentencia_while(self, ctx:ExprParser.Sentencia_whileContext):
        pass

    # Exit a parse tree produced by ExprParser#sentencia_while.
    def exitSentencia_while(self, ctx:ExprParser.Sentencia_whileContext):
        pass


    # Enter a parse tree produced by ExprParser#sentencia_for.
    def enterSentencia_for(self, ctx:ExprParser.Sentencia_forContext):
        pass

    # Exit a parse tree produced by ExprParser#sentencia_for.
    def exitSentencia_for(self, ctx:ExprParser.Sentencia_forContext):
        pass


    # Enter a parse tree produced by ExprParser#declaracion_funcion.
    def enterDeclaracion_funcion(self, ctx:ExprParser.Declaracion_funcionContext):
        nombre_funcion = ctx.VARIABLE().getText()
        tipo_retorno = ctx.tipo().getText()
        
        params = []
        if ctx.parametros():
            for param in ctx.parametros().parametro():
                param_name = param.VARIABLE().getText()
                param_type = param.tipo().getText()
                params.append((param_name, param_type))
        
        self.symbol_table.define_function(nombre_funcion, params, tipo_retorno)
        self.current_function = nombre_funcion
        
        # Crear scope para la función
        self.symbol_table.enter_scope()
        
        # Definir parámetros en el scope de la función
        for param_name, param_type in params:
            self.symbol_table.define_variable(param_name, param_type)

    # Exit a parse tree produced by ExprParser#declaracion_funcion.
    def exitDeclaracion_funcion(self, ctx:ExprParser.Declaracion_funcionContext):
        pass


    # Enter a parse tree produced by ExprParser#funcion_llamada.
    def enterFuncion_llamada(self, ctx:ExprParser.Funcion_llamadaContext):
        pass

    # Exit a parse tree produced by ExprParser#funcion_llamada.
    def exitFuncion_llamada(self, ctx:ExprParser.Funcion_llamadaContext):
        pass


    # Enter a parse tree produced by ExprParser#funcion_llamada_expr.
    def enterFuncion_llamada_expr(self, ctx:ExprParser.Funcion_llamada_exprContext):
        nombre_funcion = ctx.VARIABLE().getText()
    
        # Verificar si la función está definida
        if nombre_funcion not in self.symbol_table.funciones:
            self.report_error(ctx, f"Error: Función '{nombre_funcion}' no definida.")
            return
    
        # Verificar argumentos
        args = []
        if ctx.argumentos():
            for arg in ctx.argumentos().expr():
                arg_type = self._infer_type_from_expression(arg)
                args.append(arg_type)
    
        # Verificar que el número de argumentos coincida
        func_info = self.symbol_table.get_function(nombre_funcion)
        expected_params = func_info['params']
    
        if len(args) != len(expected_params):
            self.report_error(ctx, f"Error: La función '{nombre_funcion}' espera {len(expected_params)} argumentos, pero se proporcionaron {len(args)}.")
            return
    
        # Verificar tipos de argumentos
        for i, (arg_type, (param_name, param_type)) in enumerate(zip(args, expected_params)):
            if arg_type != param_type:
                self.report_error(ctx, f"Error: Argumento {i+1} de la función '{nombre_funcion}' debe ser de tipo '{param_type}', pero se encontró '{arg_type}'.")
                return
    
        # Asignar tipo de retorno a la expresión
        ctx.type = func_info['return_type']

    # Exit a parse tree produced by ExprParser#funcion_llamada_expr.
    def exitFuncion_llamada_expr(self, ctx:ExprParser.Funcion_llamada_exprContext):
        pass


    # Enter a parse tree produced by ExprParser#retorna.
    def enterRetorna(self, ctx:ExprParser.RetornaContext):
        if not self.current_function:
            self.report_error(ctx, "Error: Sentencia 'retorna' fuera de una función.")
            return
            
        expected_type = self.symbol_table.get_function_return_type(self.current_function)
        
        if ctx.expr():
            expr_type = self._infer_type_from_expression(ctx.expr())
            if expected_type != expr_type:
                self.report_error(ctx, 
                    f"Error: La función '{self.current_function}' debe retornar '{expected_type}' " +
                    f"pero se encontró '{expr_type if expr_type else 'None'}'")

    # Exit a parse tree produced by ExprParser#retorna.
    def exitRetorna(self, ctx:ExprParser.RetornaContext):
        pass


    # Enter a parse tree produced by ExprParser#parametros.
    def enterParametros(self, ctx:ExprParser.ParametrosContext):
        pass

    # Exit a parse tree produced by ExprParser#parametros.
    def exitParametros(self, ctx:ExprParser.ParametrosContext):
        pass


    # Enter a parse tree produced by ExprParser#parametro.
    def enterParametro(self, ctx:ExprParser.ParametroContext):
        pass

    # Exit a parse tree produced by ExprParser#parametro.
    def exitParametro(self, ctx:ExprParser.ParametroContext):
        pass


    # Enter a parse tree produced by ExprParser#argumentos.
    def enterArgumentos(self, ctx:ExprParser.ArgumentosContext):
        pass

    # Exit a parse tree produced by ExprParser#argumentos.
    def exitArgumentos(self, ctx:ExprParser.ArgumentosContext):
        pass


    # Enter a parse tree produced by ExprParser#bloque_condicional.
    def enterBloque_condicional(self, ctx:ExprParser.Bloque_condicionalContext):
        pass

    # Exit a parse tree produced by ExprParser#bloque_condicional.
    def exitBloque_condicional(self, ctx:ExprParser.Bloque_condicionalContext):
        pass


    # Enter a parse tree produced by ExprParser#bloque_de_sentencia.
    def enterBloque_de_sentencia(self, ctx:ExprParser.Bloque_de_sentenciaContext):
        pass

    # Exit a parse tree produced by ExprParser#bloque_de_sentencia.
    def exitBloque_de_sentencia(self, ctx:ExprParser.Bloque_de_sentenciaContext):
        pass


    # Enter a parse tree produced by ExprParser#declaracion.
    def enterDeclaracion(self, ctx:ExprParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by ExprParser#declaracion.
    def exitDeclaracion(self, ctx:ExprParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by ExprParser#declaracion_sin_asignacion.
    def enterDeclaracion_sin_asignacion(self, ctx:ExprParser.Declaracion_sin_asignacionContext):
        pass

    # Exit a parse tree produced by ExprParser#declaracion_sin_asignacion.
    def exitDeclaracion_sin_asignacion(self, ctx:ExprParser.Declaracion_sin_asignacionContext):
        pass


    # Enter a parse tree produced by ExprParser#reasignacion.
    def enterReasignacion(self, ctx:ExprParser.ReasignacionContext):
        pass

    # Exit a parse tree produced by ExprParser#reasignacion.
    def exitReasignacion(self, ctx:ExprParser.ReasignacionContext):
        pass


    # Enter a parse tree produced by ExprParser#tipo.
    def enterTipo(self, ctx:ExprParser.TipoContext):
        pass

    # Exit a parse tree produced by ExprParser#tipo.
    def exitTipo(self, ctx:ExprParser.TipoContext):
        pass


    # Enter a parse tree produced by ExprParser#mostrar.
    def enterMostrar(self, ctx:ExprParser.MostrarContext):
        pass

    # Exit a parse tree produced by ExprParser#mostrar.
    def exitMostrar(self, ctx:ExprParser.MostrarContext):
        pass


    # Enter a parse tree produced by ExprParser#expr.
    def enterExpr(self, ctx:ExprParser.ExprContext):
        if ctx.getChildCount() == 3:  # Operación binaria
            left = ctx.getChild(0)
            operator = ctx.getChild(1).getText()
            right = ctx.getChild(2)

            left_type = self._infer_type_from_expression(left)
            right_type = self._infer_type_from_expression(right)

            # Operadores lógicos
            if operator in ['&&', '||']:
                if left_type != 'bool' or right_type != 'bool':
                    self.report_error(ctx, f"Error: Operación lógica '{operator}' solo válida entre booleanos, pero se encontró '{left_type}' y '{right_type}'.")
                # Establecer el tipo de la expresión como bool
                ctx.type = 'bool'
                return
                
            # Operadores aritméticos
            if operator in ['+', '-', '*', '/']:
                if not (self._is_numeric_type(left_type) and self._is_numeric_type(right_type)):
                    self.report_error(ctx, f"Error: Operación '{operator}' no válida entre '{left_type}' y '{right_type}'.")
            elif operator == '%':
                if left_type != 'entero' or right_type != 'entero':
                    self.report_error(ctx, f"Error: Operación '%' solo válida entre enteros, pero se encontró '{left_type}' y '{right_type}'.")
            # Operadores de comparación
            elif operator in ['<', '>', '<=', '>=']:
                if not (self._is_numeric_type(left_type) and self._is_numeric_type(right_type)):
                    self.report_error(ctx, f"Error: Operación '{operator}' no válida entre '{left_type}' y '{right_type}'.")
                # Establecer el tipo de la expresión como bool
                ctx.type = 'bool'
            elif operator in ['==', '!=']:
                if left_type != right_type:
                    self.report_error(ctx, f"Error: Comparación '{operator}' no válida entre '{left_type}' y '{right_type}'.")
                # Establecer el tipo de la expresión como bool
                ctx.type = 'bool'

    # Exit a parse tree produced by ExprParser#expr.
    def exitExpr(self, ctx:ExprParser.ExprContext):
        pass


    # Enter a parse tree produced by ExprParser#term.
    def enterTerm(self, ctx:ExprParser.TermContext):
        pass

    # Exit a parse tree produced by ExprParser#term.
    def exitTerm(self, ctx:ExprParser.TermContext):
        pass


    # Enter a parse tree produced by ExprParser#factor.
    def enterFactor(self, ctx:ExprParser.FactorContext):
        pass

    # Exit a parse tree produced by ExprParser#factor.
    def exitFactor(self, ctx:ExprParser.FactorContext):
        pass


    # Enter a parse tree produced by ExprParser#actualizacion.
    def enterActualizacion(self, ctx:ExprParser.ActualizacionContext):
        pass

    # Exit a parse tree produced by ExprParser#actualizacion.
    def exitActualizacion(self, ctx:ExprParser.ActualizacionContext):
        pass


    # Enter a parse tree produced by ExprParser#sentencia_switch.
    def enterSentencia_switch(self, ctx:ExprParser.Sentencia_switchContext):
        pass

    # Exit a parse tree produced by ExprParser#sentencia_switch.
    def exitSentencia_switch(self, ctx:ExprParser.Sentencia_switchContext):
        pass


    def _infer_type_from_expression(self, expr_node):
        if isinstance(expr_node, TerminalNode):
            return self._get_type_from_node(expr_node)
        
        if hasattr(expr_node, 'type'):
            return expr_node.type
        
        if expr_node.getChildCount() == 1:
            return self._infer_type_from_expression(expr_node.getChild(0))
        
        if expr_node.getChildCount() == 3:  # Operación binaria
            left_type = self._infer_type_from_expression(expr_node.getChild(0))
            right_type = self._infer_type_from_expression(expr_node.getChild(2))
            operator = expr_node.getChild(1).getText()
            
            # Operadores lógicos
            if operator in ['&&', '||']:
                if left_type == 'bool' and right_type == 'bool':
                    return 'bool'
                return None
            
            # Operaciones aritméticas
            if operator in ['+', '-', '*', '/']:
                if 'decimal' in (left_type, right_type):
                    return 'decimal'
                if 'entero' in (left_type, right_type):
                    return 'entero'
                self.report_error(expr_node, f"Operación '{operator}' no válida entre {left_type} y {right_type}")
            # Comparaciones
            elif operator in ['==', '!=', '<', '>', '<=', '>=']:
                return 'bool'
            elif operator == '%':
                if left_type == 'entero' and right_type == 'entero':
                    return 'entero'
                self.report_error(expr_node, f"Operación '%' no válida entre {left_type} y {right_type}")
            elif operator == '^':
                if self._is_numeric_type(left_type) and self._is_numeric_type(right_type):
                    return 'decimal' if 'decimal' in (left_type, right_type) else 'entero'
                self.report_error(expr_node, f"Operación '^' no válida entre {left_type} y {right_type}")


del ExprParser