from ExprParser import ExprParser
from visitors.ExprBaseVisitor import *

class ExprVariableVisitor(ExprBaseVisitor):
    def __init__(self):
        super().__init__()

    def visitDeclaracion_sin_asignacion(self, ctx: ExprParser.Declaracion_sin_asignacionContext):
        var_name = ctx.VARIABLE().getText()
        var_type = ctx.tipo().getText()
        self.define_variable(var_name, None)
        return None

    def define_function(self, name, params, return_type, body):
        info = {
            'params': params,
            'return_type': return_type,
            'body': body
        }
        super().define_function(name, info)

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

    def visitDeclaracion(self, ctx: ExprParser.DeclaracionContext):
        var_name = ctx.VARIABLE().getText()
        var_type = ctx.tipo().getText()

        value = None
        inferred_type = None

        if ctx.expr():
            value = self.visit(ctx.expr())
            print("algo",value)
            inferred_type = self.traducir_tipo(value)
            print("algo infer",inferred_type)

        elif ctx.funcion_llamada():
            value = self.visit(ctx.funcion_llamada())
            nombre_funcion = ctx.funcion_llamada().VARIABLE().getText()
            inferred_type = self.get_function_return_type(nombre_funcion)
            print(f"Llamada a función '{nombre_funcion}' devuelve tipo '{inferred_type}' con valor: {value}")

        else:
            raise ValueError(f"La declaración de '{var_name}' no tiene una expresión o llamada de función válida.")

        # Verificación de tipo
        if var_type != inferred_type:
            raise TypeError(
                f"Error de tipo: Se esperaba '{var_type}' para '{var_name}', pero se obtuvo '{inferred_type}'"
            )

        self.define_variable(var_name, value)
        return value


    def visitReasignacion(self, ctx: ExprParser.ReasignacionContext):
        var_name = ctx.VARIABLE().getText()
        new_value = self.visit(ctx.expr())

        try:
            original_value = self.get_variable(var_name)
        except NameError:
            raise NameError(f"Error: La variable '{var_name}' no está definida antes de reasignarla")

        if isinstance(original_value, int) and not isinstance(new_value, int):
            raise TypeError(f"La variable '{var_name}' es un entero, pero se intentó asignar {self.traducir_tipo(new_value)}")
        elif isinstance(original_value, float) and not isinstance(new_value, float):
            raise TypeError(f"La variable '{var_name}' es un decimal, pero se intentó asignar {self.traducir_tipo(new_value)}")
        elif isinstance(original_value, str) and not isinstance(new_value, str):
            raise TypeError(f"La variable '{var_name}' es una cadena, pero se intentó asignar {self.traducir_tipo(new_value)}")
        elif isinstance(original_value, bool) and not isinstance(new_value, bool):
            raise TypeError(f"La variable '{var_name}' es un bool, pero se intentó asignar {self.traducir_tipo(new_value)}")

        self.define_variable(var_name, new_value)
        return new_value

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
