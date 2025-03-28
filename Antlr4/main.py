import sys
import logging
import traceback
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ExprListener import ExprListener
from PersonalizatedVisitor import PersonalizatedVisitor
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
        # Log de error con detalles adicionales de la línea y columna
        error_logger.error(f"Error en la línea {line}, columna {column}: {msg}")
    
    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        error_message = f"Ambigüedad detectada entre los índices {startIndex}-{stopIndex}"
        print(error_message)
        error_logger.warning(error_message)
    
    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts):
        error_message = f"Intento de análisis de contexto completo entre los índices {startIndex}-{stopIndex}"
        print(error_message)
        error_logger.warning(error_message)
    
    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts):
        error_message = f"Confusión en el contexto de los índices {startIndex}-{stopIndex}"
        print(error_message)
        error_logger.warning(error_message)

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
        # Definir el archivo de entrada
        path_file = "bad-input-files/bad-entero_decimal.txt"  # Cambia la ruta a tu archivo de entrada
        
        if not checkExtension(path_file):
            raise ValueError("El archivo debe tener una extensión .txt")
        
        input_stream = FileStream(path_file)  # Expresión que quieres analizar
        lexer = ExprLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = ExprParser(token_stream)

        # Añadir el listener de errores
        parser.addErrorListener(MyErrorListener())

        # Generar el árbol de análisis
        tree = parser.gramatica()  # Cambia esta regla según tu gramática

        print("Análisis sintáctico completado correctamente.")
        prettyPrintTree(tree, parser)  # Imprime el árbol de análisis para verificar la estructura

        # Crear y añadir el listener personalizado
        listener = ExprListener()  # Si necesitas personalizarlo, hereda de ExprListener
        walker = ParseTreeWalker()  # Usamos ParseTreeWalker para caminar por el árbol
        walker.walk(listener, tree)  # El listener ahora escuchará los eventos del árbol

        # Evaluar la expresión usando ExprVisitor
        visitor = PersonalizatedVisitor()  # El visitor personalizado para evaluar el árbol
        result = visitor.visit(tree)  # Evaluamos el árbol utilizando el visitor
        print(f"Resultado de la evaluación: {result}")  # Imprimimos el resultado de la evaluación

        # Log de éxito
        if result is None:
            error_logger.error(f"Error en la evaluación: {result}")
        
        success_logger.info("Análisis sintáctico completado correctamente para la expresión válida.")
        success_logger.info(f"Resultado de la evaluación: {result}")

    except FileNotFoundError as fnf_error:
        # Captura errores de archivo no encontrado
        print(f"Archivo no encontrado: {fnf_error}")
        error_logger.error(f"Archivo no encontrado: {fnf_error}")
    except ValueError as ve:
        # Captura errores de valor como problemas de extensión de archivo
        print(f"Error de valor: {ve}")
        error_logger.error(f"Error de valor: {ve}")
    except Exception as e:
        # Captura cualquier otro tipo de excepción
        print(f"Ocurrió un error: {e}")
        traceback.print_exc()  # Esto imprime más detalles sobre el error
        error_logger.error(f"Ocurrió un error durante el análisis: {e}")
        error_logger.error(f"Detalles del error: {traceback.format_exc()}")

if __name__ == "__main__":
    main()
