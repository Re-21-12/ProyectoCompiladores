from antlr4 import *
from ExprParser import ExprParser

class ExprBaseVisitor(ParseTreeVisitor):
    def __init__(self):
        self.variables = {}

    def traducir_tipo(self, tipo):
        if isinstance(tipo, int):
            return "entero"
        elif isinstance(tipo, float):
            return "decimal"
        else:
            raise ValueError(f"El tipo de dato no es el correcto: {tipo}")
