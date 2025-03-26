from ExprParser import ExprParser
from  ExprBaseVisitor import ExprBaseVisitor


class ExprVariableVisitor(ExprBaseVisitor):

    def visitDeclaracion(self, ctx: ExprParser.DeclaracionContext):
        var_name = ctx.VARIABLE().getText()
        var_type = ctx.tipo().getText()
        value = self.visit(ctx.expr())

        if var_type == "entero" and not isinstance(value, int):
            raise TypeError(f"Error de tipo: Se esperaba un entero para '{var_name}', pero se obtuvo {self.traducir_tipo(value)}")
        elif var_type == "decimal" and not isinstance(value, float):
            raise TypeError(f"Error de tipo: Se esperaba un decimal para '{var_name}', pero se obtuvo {self.traducir_tipo(value)}")

        self.variables[var_name] = value
        return value

    def visitReasignacion(self, ctx: ExprParser.ReasignacionContext):
        var_name = ctx.VARIABLE().getText()
        new_value = self.visit(ctx.expr())

        if var_name in self.variables:
            original_value = self.variables[var_name]

            if isinstance(original_value, int) and not isinstance(new_value, int):
                raise TypeError(f"La variable '{var_name}' es un entero, pero se intentó asignar {self.traducir_tipo(new_value)}")
            elif isinstance(original_value, float) and not isinstance(new_value, float):
                raise TypeError(f"La variable '{var_name}' es un decimal, pero se intentó asignar {self.traducir_tipo(new_value)}")

            self.variables[var_name] = new_value
        else:
            raise NameError(f"Variable no definida: {var_name}")

        return new_value
