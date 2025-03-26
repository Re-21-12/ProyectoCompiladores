from ExprParser import ExprParser
from  visitors.ExprBaseVisitor import *

class ExprVariableVisitor(ExprBaseVisitor):

    def visitDeclaracion(self, ctx: ExprParser.DeclaracionContext):
        var_name = ctx.VARIABLE().getText()
        var_type = ctx.tipo().getText()
        value = self.visit(ctx.expr())

        if var_type == "entero" and not isinstance(value, int):
            raise TypeError(f"Error de tipo: Se esperaba un entero para '{var_name}', pero se obtuvo {ExprBaseVisitor.traducir_tipo(value)}")
        elif var_type == "decimal" and not isinstance(value, float):
            raise TypeError(f"Error de tipo: Se esperaba un decimal para '{var_name}', pero se obtuvo {ExprBaseVisitor.traducir_tipo(value)}")
        elif var_type == "cadena" and not isinstance(value, str):
            raise TypeError(f"Error de tipo: Se esperaba una cadena  para '{var_name}', pero se obtuvo {ExprBaseVisitor.traducir_tipo(value)}")
        elif var_type == "bool" and not isinstance(value, bool):
            raise TypeError(f"Error de tipo: Se esperaba un bool  para '{var_name}', pero se obtuvo {ExprBaseVisitor.traducir_tipo(value)}")


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
            elif isinstance(original_value, str) and not isinstance(new_value, str):
                raise TypeError(f"La variable '{var_name}' es una cadena, pero se intentó asignar {self.traducir_tipo(new_value)}")
            elif isinstance(original_value, bool) and not isinstance(new_value, bool):
                raise TypeError(f"La variable '{var_name}' es un bool, pero se intentó asignar {self.traducir_tipo(new_value)}")

            # Si pasa todas las validaciones, actualizar el valor
            self.variables[var_name] = new_value
        else:
            raise NameError(f"Variable no definida: {var_name}")

        return new_value


    def visitActualizacion(self, ctx: ExprParser.ActualizacionContext):
        var_name = ctx.VARIABLE().getText()
        print(f"Actualizando variable: {var_name}")
 
        if var_name not in self.variables:
            raise NameError(f"Variable no definida: {var_name}")
 
        if ctx.MASMAS():
            print(f"Incrementando {var_name}")
            self.variables[var_name] += 1
        elif ctx.MENOSMENOS():
            print(f"Decrementando {var_name}")
            self.variables[var_name] -= 1
        elif ctx.expr():
            new_value = self.visit(ctx.expr())
            self.variables[var_name] = new_value
 
        print(f"Nuevo valor de {var_name}: {self.variables[var_name]}")
        return self.variables[var_name]