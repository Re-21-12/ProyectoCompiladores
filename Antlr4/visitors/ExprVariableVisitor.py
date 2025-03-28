from ExprParser import ExprParser
from visitors.ExprBaseVisitor import *

class ExprVariableVisitor(ExprBaseVisitor):

    def visitDeclaracion(self, ctx: ExprParser.DeclaracionContext):
        var_name = ctx.VARIABLE().getText()
        var_type = ctx.tipo().getText()
        value = self.visit(ctx.expr())

        if var_type == "entero" and not isinstance(value, int):
            raise TypeError(f"Error de tipo: Se esperaba un entero para '{var_name}', pero se obtuvo {self.traducir_tipo(value)}")
        elif var_type == "decimal" and not isinstance(value, float):
            raise TypeError(f"Error de tipo: Se esperaba un decimal para '{var_name}', pero se obtuvo {self.traducir_tipo(value)}")
        elif var_type == "cadena" and not isinstance(value, str):
            raise TypeError(f"Error de tipo: Se esperaba una cadena para '{var_name}', pero se obtuvo {self.traducir_tipo(value)}")
        elif var_type == "bool" and not isinstance(value, bool):
            raise TypeError(f"Error de tipo: Se esperaba un bool para '{var_name}', pero se obtuvo {self.traducir_tipo(value)}")
        
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
        return super().visitActualizacion(ctx)

    def traducir_tipo(self, value):
        """Devuelve una representación de tipo para los errores."""
        if isinstance(value, int):
            return "entero"
        elif isinstance(value, float):
            return "decimal"
        elif isinstance(value, str):
            return "cadena"
        elif isinstance(value, bool):
            return "bool"
        return "desconocido"
