import sys
import logging
# import traceback
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ExprListener import ExprListener
from PersonalizatedListener import PersonalizatedListener
from PersonalizatedVisitor import PersonalizatedVisitor
from ASTVisitor import ASTVisitor
from PersonalizatedLlvmlite import LLVMGenerator
from antlr4.tree.Trees import Trees
from colorama import init, Fore, Back, Style
import pyfiglet
import subprocess
from pathlib import Path

# Inicializar colorama
init(autoreset=True)

# Configuración de logs con colores
class ColoredFormatter(logging.Formatter):
    COLORS = {
        'WARNING': Fore.YELLOW,
        'ERROR': Fore.RED,
        'CRITICAL': Fore.RED + Back.WHITE,
        'INFO': Fore.GREEN
    }

    def format(self, record):
        color = self.COLORS.get(record.levelname, '')
        message = super().format(record)
        return color + message

# Configuración de los logs
success_handler = logging.FileHandler("logs/log_success.txt")
error_handler = logging.FileHandler("logs/log_error.txt")
console_handler = logging.StreamHandler()

# Formateadores
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
colored_formatter = ColoredFormatter("%(asctime)s - %(levelname)s - %(message)s")

success_handler.setFormatter(formatter)
error_handler.setFormatter(formatter)
console_handler.setFormatter(colored_formatter)

# Loggers
success_logger = logging.getLogger("SuccessLogger")
error_logger = logging.getLogger("ErrorLogger")

success_logger.addHandler(success_handler)
error_logger.addHandler(error_handler)
error_logger.addHandler(console_handler)

success_logger.setLevel(logging.INFO)
error_logger.setLevel(logging.ERROR)


def print_banner():
    banner = pyfiglet.figlet_format("Expr Analyzer", font="slant")
    print(f"{Fore.BLUE}{banner}{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}═" * 70)
    print(f"{Fore.CYAN}  Analizador Sintáctico para Gramática Expr")
    print(f"{Fore.MAGENTA}═" * 70 + Style.RESET_ALL)

def print_section(title, color=Fore.GREEN):
    print(f"\n{color}┌{'─' * (len(title)+2)}┐")
    print(f"│ {title.upper()} │")
    print(f"└{'─' * (len(title)+2)}┘{Style.RESET_ALL}")

def pretty_print_tree(tree, parser, indent=0, last=True, prefix=''):
    """Imprime el árbol de análisis con formato visual mejorado"""
    # Obtener el texto del nodo
    if isinstance(tree, TerminalNode):
        text = tree.getText()
        symbol_type = parser.symbolicNames[tree.getSymbol().type]
        print(f"{prefix}{'└── ' if last else '├── '}{Fore.CYAN}{text} ({symbol_type}){Style.RESET_ALL}")
        return
    
    # Para nodos no terminales
    rule_name = parser.ruleNames[tree.getRuleIndex()]
    
    if indent == 0:
        print(f"{Fore.YELLOW}Árbol de Análisis Sintáctico:{Style.RESET_ALL}")
    
    # Determinar el prefijo y símbolo de rama
    branch = '└── ' if last else '├── '
    new_prefix = prefix + ("    " if last else "│   ")
    
    print(f"{prefix}{branch}{Fore.GREEN}{rule_name}{Style.RESET_ALL}")
    
    # Recorrer hijos - convertimos el generador a lista
    children = list(tree.getChildren())
    if children:
        for i, child in enumerate(children):
            pretty_print_tree(child, parser, indent+1, i == len(children)-1, new_prefix)

def check_extension(text):
    return text.endswith('.txt')
def compile_and_run(llvm_ir):
    """Compila y ejecuta el código LLVM generado"""
    try:
        # Crear directorio de salida si no existe
        output_dir = Path("outputs")
        output_dir.mkdir(exist_ok=True)
        
        # 1. Guardar el IR LLVM
        ll_file = output_dir/"output.ll"
        with open(ll_file, "w") as f:
            f.write(str(llvm_ir))
        print(f"{Fore.GREEN}✔ IR LLVM guardado en: {ll_file}{Style.RESET_ALL}")
        
        # 2. Compilar a código objeto
        obj_file = output_dir/"output.o"
        subprocess.run(
            ["llc", "-filetype=obj", str(ll_file), "-o", str(obj_file)],
            check=True,
            stderr=subprocess.PIPE
        )
        print(f"{Fore.GREEN}✔ Objeto compilado en: {obj_file}{Style.RESET_ALL}")
        
        # 3. Generar ensamblador (opcional)
        asm_file = output_dir/"output.s"
        subprocess.run(
            ["llc", "-march=x86-64", str(ll_file), "-o", str(asm_file)],
            check=True,
            stderr=subprocess.PIPE
        )
        print(f"{Fore.GREEN}✔ Ensamblador generado en: {asm_file}{Style.RESET_ALL}")
        
        # 4. Optimizar (opcional)
        opt_file = output_dir/"optimized.ll"
        subprocess.run(
            ["opt", "-O3", "-S", str(ll_file), "-o", str(opt_file)],
            check=True,
            stderr=subprocess.PIPE
        )
        print(f"{Fore.GREEN}✔ Versión optimizada en: {opt_file}{Style.RESET_ALL}")
        
        # 5. Enlazar y crear ejecutable
        exec_file = output_dir/"program"
        subprocess.run(
            ["clang", str(obj_file), "-o", str(exec_file)],
            check=True,
            stderr=subprocess.PIPE
        )
        print(f"{Fore.GREEN}✔ Ejecutable creado en: {exec_file}{Style.RESET_ALL}")
        
        # 6. Ejecutar el programa
        print(f"\n{Fore.YELLOW}═"*50)
        print(f"{Fore.CYAN}  EJECUCIÓN DEL PROGRAMA  ")
        print(f"{Fore.YELLOW}═"*50 + Style.RESET_ALL)
        
        result = subprocess.run(
            [str(exec_file)],
            capture_output=True,
            text=True
        )
        
        if result.stdout:
            print(f"{Fore.GREEN}Salida:\n{result.stdout}{Style.RESET_ALL}")
        if result.stderr:
            print(f"{Fore.RED}Errores:\n{result.stderr}{Style.RESET_ALL}")
            
        return True
        
    except subprocess.CalledProcessError as e:
        error_msg = f"{Fore.RED}✖ Error en compilación: {e.stderr}{Style.RESET_ALL}"
        print(error_msg)
        error_logger.error(error_msg)
        return False
    except Exception as e:
        error_msg = f"{Fore.RED}✖ Error inesperado: {str(e)}{Style.RESET_ALL}"
        print(error_msg)
        error_logger.error(error_msg)
        return False
"""
==========================================
==========================================
==============MAIN=======================
==========================================
==========================================
"""
def main():
    print_banner()
    
    try:
        # Definir archivo de entrada
        #path_file = "bad-input-files/bad-actualizacion.txt"
        path_file = "good-input-files/actualizar.txt"
        
        print_section("configuración inicial")
        print(f"{Fore.WHITE}Analizando archivo: {Fore.YELLOW}{path_file}{Style.RESET_ALL}")
        
        if not check_extension(path_file):
            raise ValueError("El archivo debe tener extensión .txt")
        
        # Procesamiento del input
        input_stream = FileStream(path_file)
        lexer = ExprLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = ExprParser(token_stream)

        # Añadir listener de errores
        parser.removeErrorListeners()
        parser.addErrorListener(PersonalizatedListener())


        print_section("análisis sintáctico")
        tree = parser.gramatica()
        
        # Visualización del árbol
        print_section("estructura del árbol", Fore.BLUE)
        pretty_print_tree(tree, parser)
        
        # Evaluación
        print_section("ejecución del listener", Fore.YELLOW)
        listener = PersonalizatedListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        
        print_section("evaluación visitor", Fore.MAGENTA)
        visitor = PersonalizatedVisitor()
        result = visitor.visit(tree)
        
        ast_visitor = ASTVisitor()
        ast_result = ast_visitor.visit(tree)
        print(f"\n{Fore.GREEN}✔ Análisis completado{Style.RESET_ALL}")
        
        # Logs
        success_logger.info(f"Análisis exitoso para {path_file}")
        print_section("AST generado", Fore.CYAN)
        print(ast_result)
    
        logging.info("Generando código LLVM...")
        llvm_generator = LLVMGenerator()
        llvm_code = llvm_generator.generate(ast_result)
        output_file = llvm_generator.save_to_file()
        print(f"IR generado y guardado en: {output_file}")
        logging.info("Código LLVM generado :")
        print(llvm_code)
        
        logging.info("Compilando y Corriendo...")
        if not compile_and_run(str(llvm_code)):
            print(f"{Fore.RED}✖ Fallo en la compilación o ejecución{Style.RESET_ALL}")
    
    except FileNotFoundError as fnf_error:
        error_msg = f"{Fore.RED}✖ Archivo no encontrado: {fnf_error}{Style.RESET_ALL}"
        print(error_msg)
        error_logger.error(error_msg)
    except ValueError as ve:
        error_msg = f"{Fore.RED}✖ Error de valor: {ve}{Style.RESET_ALL}"
        print(error_msg)
        error_logger.error(error_msg)
    # except Exception as e:
    #     error_msg = f"\n{Fore.RED}✖ Error inesperado:\n{Fore.WHITE}{traceback.format_exc()}{Style.RESET_ALL}"
    #     error_logger.error(f"Error inesperado: {e}\n{traceback.format_exc()}")

if __name__ == "__main__":
    main()