import sys
import logging
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
# antlr4 -Dlanguage=Python3 -visitor Expr.g4
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ExprVisitor import ExprVisitor

from antlr4.tree.Trees import Trees

# Configuración de los logs
success_handler = logging.FileHandler("logs/log_success.txt")
error_handler = logging.FileHandler("logs/log_error.txt")

# Formato común para los logs
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
success_handler.setFormatter(formatter)
error_handler.setFormatter(formatter)




# Creación de los loggers
success_logger = logging.getLogger("SuccessLogger")
error_logger = logging.getLogger("ErrorLogger")

# Asignar manejadores a los loggers
success_logger.addHandler(success_handler)
error_logger.addHandler(error_handler)

# Establecer niveles de log
success_logger.setLevel(logging.INFO)
error_logger.setLevel(logging.ERROR)

# Definición del ErrorListener personalizado
class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_message = f"Error de sintaxis en la línea {line}, columna {column}: {msg}"
        print(error_message)
        error_logger.error(error_message)

def prettyPrintTree(tree, parser, indent=0):
    """Imprime el árbol de análisis de forma estructurada."""
    if tree.getChildCount() == 0:
        print("  " * indent + str(tree.getText()))
    else:
        print("  " * indent + parser.ruleNames[tree.getRuleIndex()])
        for i in range(tree.getChildCount()):
            prettyPrintTree(tree.getChild(i), parser, indent + 1)

def checkExtension(text):
    return text.endswith('.txt') 

def main():
    try:
        # path_file = "good-input-files/entero_decimal.txt"
        path_file = "bad-input-files/bad-entero_decimal.txt"
        
        if not checkExtension(path_file):
            raise ValueError("El archivo debe tener una extensión .txt")
        
        input_stream = FileStream(path_file)  # Expresión que quieres analizar
        lexer = ExprLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = ExprParser(token_stream)
        parser.addErrorListener(MyErrorListener())  # Añadir el listener de errores
        tree = parser.gramatica()  # Cambiar regla de entrada específica
        
        print("Análisis sintáctico completado correctamente.")
        prettyPrintTree(tree, parser)
        
        # Evaluar la expresión usando ExprVisitor
        visitor = ExprVisitor()
        result = visitor.visit(tree)  # Evaluamos el árbol utilizando el visitor
        print(f"Resultado de la evaluación: {result}")  # Imprimmimos el resultado de la evaluación
        
        # Log de éxito
        if result is None:
            error_logger.error(f"Error en la evaluación: {result}")
            
        success_logger.info("Análisis sintáctico completado correctamente para la expresión válida.")
        success_logger.info(f"Resultado de la evaluación: {result}")

    except Exception as e:
        # En caso de error, mostramos el mensaje y lo guardamos en el log de errores
        print(f"Ocurrió un error: {e}")
        error_logger.error(f"Ocurrió un error durante el análisis: {e}")

if __name__ == "__main__":
    main()
