import sys
import logging
import traceback
from antlr4 import *

from antlr4.error.ErrorListener import ErrorListener
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from PersonalizatedListener import PersonalizatedListener
from PersonalizatedVisitor import PersonalizatedVisitor
from antlr4.tree.Trees import Trees

# Configuración avanzada de logging
def setup_logging():
    """Configura el sistema de logging con handlers y formatters"""
    # Handlers para archivos
    success_handler = logging.FileHandler("logs/log_success.txt", mode='w')
    error_handler = logging.FileHandler("logs/log_error.txt", mode='w')
    console_handler = logging.StreamHandler()
    
    # Formateadores
    file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    console_formatter = logging.Formatter("%(levelname)s - %(message)s")
    
    # Configurar handlers
    success_handler.setFormatter(file_formatter)
    error_handler.setFormatter(file_formatter)
    console_handler.setFormatter(console_formatter)
    
    # Configurar loggers
    success_logger = logging.getLogger("SuccessLogger")
    error_logger = logging.getLogger("ErrorLogger")
    console_logger = logging.getLogger("ConsoleLogger")
    
    # Asignar niveles y handlers
    success_logger.setLevel(logging.INFO)
    error_logger.setLevel(logging.ERROR)
    console_logger.setLevel(logging.INFO)
    
    success_logger.addHandler(success_handler)
    error_logger.addHandler(error_handler)
    console_logger.addHandler(console_handler)
    
    return success_logger, error_logger, console_logger

class EnhancedErrorListener(ErrorListener):
    """Listener de errores mejorado con logging detallado"""
    def __init__(self, error_logger, console_logger):
        super().__init__()
        self.error_logger = error_logger
        self.console_logger = console_logger
    
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_message = f"Error de sintaxis en línea {line}, columna {column}: {msg}"
        self.console_logger.error(error_message)
        self.error_logger.error(error_message)
        # Modo pánico: podrías añadir lógica para recuperación aquí

def prettyPrintTree(tree, parser, indent=0):
    """Imprime el árbol de análisis de forma estructurada con colores"""
    from colorama import init, Fore
    init()  # Inicializa colorama
    
    if tree.getChildCount() == 0:
        print("  " * indent + Fore.GREEN + str(tree.getText()) + Fore.RESET)
    else:
        print("  " * indent + Fore.BLUE + parser.ruleNames[tree.getRuleIndex()] + Fore.RESET)
        for i in range(tree.getChildCount()):
            prettyPrintTree(tree.getChild(i), parser, indent + 1)

def validate_file(path):
    """Valida el archivo de entrada"""
    if not path.endswith('.txt'):
        raise ValueError("El archivo debe tener extensión .txt")
    try:
        with open(path, 'r') as f:
            content = f.read(1)  # Lee solo el primer byte para verificar acceso
        return True
    except Exception as e:
        raise IOError(f"No se pudo leer el archivo: {str(e)}")

def display_symbol_table(symbol_table, logger):
    """Muestra la tabla de símbolos de forma organizada"""
    if not symbol_table:
        logger.info("Tabla de símbolos vacía")
        return
    
    logger.info("\n=== TABLA DE SÍMBOLOS ===")
    for scope in symbol_table:
        logger.info("\nÁmbito:")
        for name, info in scope.items():
            logger.info(f"  {name}: {info}")

def display_functions(functions, logger):
    """Muestra las funciones declaradas"""
    if not functions:
        logger.info("No hay funciones declaradas")
        return
    
    logger.info("\n=== FUNCIONES DECLARADAS ===")
    for name, func in functions.items():
        params = ", ".join([f"{p[0]}:{p[1]}" for p in func['params']])
        logger.info(f"  {name}({params}) -> {func.get('return_type', 'void')}")

def main():
    # Configura logging
    success_logger, error_logger, console_logger = setup_logging()
    
    try:
        # Selección de archivo de entrada
        path_file = "good-input-files/funcion.txt"
        # path_file = "bad-input-files/bad-entero_decimal.txt"  # Para probar detección de errores
        
        # Validar archivo
        validate_file(path_file)
        console_logger.info(f"\nProcesando archivo: {path_file}")
        
        # 1. Análisis léxico y sintáctico
        input_stream = FileStream(path_file, encoding='utf-8')
        lexer = ExprLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = ExprParser(token_stream)
        parser.addErrorListener(EnhancedErrorListener(error_logger, console_logger))
        
        try:
            tree = parser.gramatica()
            console_logger.info("\n=== ÁRBOL DE ANÁLISIS SINTÁCTICO ===")
            prettyPrintTree(tree, parser)
            success_logger.info("Análisis sintáctico completado sin errores")
        except Exception as e:
            error_msg = f"Error crítico en análisis sintáctico: {str(e)}"
            console_logger.error(error_msg)
            error_logger.error(error_msg)
            raise
        
        # 2. Análisis semántico con el Listener
        console_logger.info("\n=== ANÁLISIS SEMÁNTICO ===")
        listener = PersonalizatedListener()
        walker = ParseTreeWalker()
        
        try:
            walker.walk(listener, tree)
            
            # Mostrar información semántica
            if hasattr(listener, 'symbol_table_stack'):
                display_symbol_table(listener.symbol_table_stack, console_logger)
                display_symbol_table(listener.symbol_table_stack, success_logger)
            
            if hasattr(listener, 'functions'):
                display_functions(listener.functions, console_logger)
                display_functions(listener.functions, success_logger)
            
            # Resultados del análisis semántico
            if listener.errors:
                console_logger.error("\nERRORES SEMÁNTICOS ENCONTRADOS:")
                for error in listener.errors:
                    console_logger.error(f" - {error}")
                    error_logger.error(error)
            else:
                console_logger.info("\n✓ Análisis semántico completado sin errores")
                success_logger.info("Análisis semántico completado sin errores")
            
            if listener.warnings:
                console_logger.warning("\nADVERTENCIAS:")
                for warning in listener.warnings:
                    console_logger.warning(f" - {warning}")
                    success_logger.warning(warning)
        
        except Exception as e:
            error_msg = f"Error en análisis semántico: {str(e)}"
            console_logger.error(error_msg)
            error_logger.error(error_msg)
            raise
        
        # 3. Evaluación con el Visitor (solo si no hay errores semánticos)
        if not listener.errors:
            console_logger.info("\n=== EVALUACIÓN DEL PROGRAMA ===")
            visitor = PersonalizatedVisitor()
            
            # Transferir información del listener al visitor
            if hasattr(listener, 'symbol_table_stack'):
                visitor.variables = listener.symbol_table_stack[0]  # Variables globales
                visitor.functions = listener.functions  # Funciones declaradas
            
            try:
                result = visitor.visit(tree)
                
                if result is not None:
                    console_logger.info(f"\nRESULTADO FINAL: {result}")
                    success_logger.info(f"Resultado de evaluación: {result}")
                else:
                    console_logger.info("\n✓ Programa ejecutado correctamente (sin valor de retorno)")
                    success_logger.info("Programa ejecutado correctamente (sin valor de retorno)")
            
            except Exception as e:
                error_msg = f"Error durante la evaluación: {str(e)}"
                console_logger.error(error_msg)
                error_logger.error(error_msg)
                raise
        
        # Resumen final
        if listener.errors:
            console_logger.error("\n✗ Proceso completado con errores")
            error_logger.error("Proceso completado con errores")
        else:
            console_logger.info("\n✓ Proceso completado exitosamente")
            success_logger.info("Proceso completado exitosamente")
    
    except Exception as e:
        error_msg = f"\nERROR INESPERADO: {str(e)}"
        console_logger.error(error_msg)
        error_logger.error(error_msg)
        error_logger.error(traceback.format_exc())
        console_logger.debug("Detalles del error:", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()