import sys
import logging
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
import time
import os
from llvmlite import ir
from llvmlite.ir import Constant, IRBuilder
import llvmlite.binding as llvm
import shutil
import platform
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
log_dir = os.path.join("..", "logs")

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

class TimeMeasurer:
    def __init__(self):
        self.phases = {}
        self.current_phase = None
        self.start_time = None
    
    def start_phase(self, phase_name):
        if self.current_phase is not None:
            self.end_phase()
        self.current_phase = phase_name
        self.start_time = time.time()
        print(f"\n{Fore.YELLOW}▶ Iniciando fase: {phase_name}{Style.RESET_ALL}")
    
    def end_phase(self):
        if self.current_phase is None:
            return
        elapsed = time.time() - self.start_time
        self.phases[self.current_phase] = elapsed
        print(f"{Fore.CYAN}⏱  Tiempo {self.current_phase}: {elapsed:.4f} segundos{Style.RESET_ALL}")
        self.current_phase = None
    
    def print_report(self):
        print(f"\n{Fore.YELLOW}=== REPORTE DE TIEMPOS ===")
        for phase, elapsed in self.phases.items():
            print(f"{Fore.CYAN}{phase}: {elapsed:.4f} segundos")
        total = sum(self.phases.values())
        print(f"\n{Fore.GREEN}TOTAL: {total:.4f} segundos{Style.RESET_ALL}")

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
    if isinstance(tree, TerminalNode):
        text = tree.getText()
        symbol_type = parser.symbolicNames[tree.getSymbol().type]
        print(f"{prefix}{'└── ' if last else '├── '}{Fore.CYAN}{text} ({symbol_type}){Style.RESET_ALL}")
        return
    
    rule_name = parser.ruleNames[tree.getRuleIndex()]
    
    if indent == 0:
        print(f"{Fore.YELLOW}Árbol de Análisis Sintáctico:{Style.RESET_ALL}")
    
    branch = '└── ' if last else '├── '
    new_prefix = prefix + ("    " if last else "│   ")
    
    print(f"{prefix}{branch}{Fore.GREEN}{rule_name}{Style.RESET_ALL}")
    
    children = list(tree.getChildren())
    if children:
        for i, child in enumerate(children):
            pretty_print_tree(child, parser, indent+1, i == len(children)-1, new_prefix)

def check_extension(text):
    return text.endswith('.txt')

def compile_llvm_ir(llvm_ir, optimize=False, generate_executable=True, run_program=False, target_exe=False):
    """Compila código LLVM IR a ejecutable (nativo o .exe para Windows)
    
    Args:
        llvm_ir: Código LLVM IR
        optimize: Aplica optimizaciones con `opt` si es True
        generate_executable: Genera ejecutable si es True
        run_program: Ejecuta el binario generado si es True
        target_exe: Genera .exe para Windows si es True
    """
    try:
        output_dir = Path("outputs")
        output_dir.mkdir(exist_ok=True)
        
        ll_file = output_dir / "output.ll"
        with open(ll_file, "w", encoding='utf-8') as f:
            f.write(str(llvm_ir))
        print(f"{Fore.GREEN}✔ IR LLVM guardado en: {ll_file}{Style.RESET_ALL}")

        # Optimización
        if optimize:
            opt_file = output_dir / "optimized.ll"
            opt_cmd = ["opt", "-O2", "-S", str(ll_file), "-o", str(opt_file)]
            result = subprocess.run(opt_cmd, capture_output=True, text=True)
            if result.stderr:
                print(f"{Fore.YELLOW}⚠ Optimización: {result.stderr}{Style.RESET_ALL}")
            print(f"{Fore.GREEN}✔ LLVM IR optimizado: {opt_file}{Style.RESET_ALL}")
            ll_file = opt_file

        if not generate_executable:
            return True

        # Compilación a código objeto
        obj_file = output_dir / "output.o"
        llc_cmd = [
            "llc",
            "-filetype=obj",
            "-O3",
        ]

        if target_exe:
            llc_cmd.extend(["-mtriple=x86_64-pc-windows-gnu"])
        llc_cmd.extend([str(ll_file), "-o", str(obj_file)])

        print(f"{Fore.CYAN}[INFO] Ejecutando llc: {' '.join(llc_cmd)}{Style.RESET_ALL}")
        result_llc = subprocess.run(llc_cmd, capture_output=True, text=True)
        if result_llc.returncode != 0:
            print(f"{Fore.RED}[ERROR] llc falló:\n{result_llc.stderr}{Style.RESET_ALL}")
            return False
        print(f"{Fore.GREEN}✔ Archivo objeto generado: {obj_file}{Style.RESET_ALL}")

        # Enlazado
        exe_file = output_dir / ("program.exe" if target_exe else "program")
        if target_exe:
            gcc_cmd = [
                "x86_64-w64-mingw32-gcc",
                str(obj_file),
                "-o", str(exe_file)
            ]
        else:
            gcc_cmd = [
                "gcc",
                str(obj_file),
                "-o", str(exe_file)
            ]

        print(f"{Fore.CYAN}[INFO] Enlazando ejecutable: {' '.join(gcc_cmd)}{Style.RESET_ALL}")
        result_gcc = subprocess.run(gcc_cmd, capture_output=True, text=True)
        if result_gcc.returncode != 0:
            print(f"{Fore.RED}[ERROR] Enlace fallido:\n{result_gcc.stderr}{Style.RESET_ALL}")
            return False
        print(f"{Fore.GREEN}✔ Ejecutable generado: {exe_file}{Style.RESET_ALL}")

        if run_program:
            print(f"{Fore.MAGENTA}▶ Ejecutando el programa:{Style.RESET_ALL}")
            subprocess.run([str(exe_file)])

        return True

    except Exception as e:
        print(f"{Fore.RED}[EXCEPCIÓN] {e}{Style.RESET_ALL}")
        return False

def compile_existing_llvm(input_ll_file, optimize=False):
    """Compila un archivo .ll existente"""
    try:
        if not os.path.exists(input_ll_file):
            raise FileNotFoundError(f"Archivo {input_ll_file} no encontrado")
            
        with open(input_ll_file, 'r', encoding='utf-8') as f:
            llvm_ir = f.read()
            
        return compile_llvm_ir(llvm_ir, optimize=optimize, generate_executable=True, run_program=False)
    except Exception as e:
        print(f"{Fore.RED}✖ Error al procesar archivo .ll: {str(e)}{Style.RESET_ALL}")
        return False


def convert_to_exe(input_file):
    """Convierte un binario a .exe (simulado)"""
    try:
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Archivo {input_file} no encontrado")

        output_dir = Path("outputs")
        output_dir.mkdir(exist_ok=True)  # Crear el directorio si no existe

        exec_file = output_dir / "program.exe"

        # En sistemas Unix, simplemente copiamos el archivo (simulación)
        shutil.copy(input_file, exec_file)

        print(f"{Fore.GREEN}✔ Ejecutable Windows creado en: {exec_file}{Style.RESET_ALL}")
        return True

    except Exception as e:
        print(f"{Fore.RED}✖ Error al convertir a .exe: {str(e)}{Style.RESET_ALL}")
        return False

def show_file_menu():
    """Muestra un menú interactivo para seleccionar archivos de prueba"""
    input_dirs = [
        "good-input-files",
        "bad-input-files"
    ]
    
    available_files = []
    for input_dir in input_dirs:
        if os.path.exists(input_dir) and os.path.isdir(input_dir):
            for file in os.listdir(input_dir):
                if file.endswith('.txt'):
                    full_path = str(Path(input_dir) / file)
                    available_files.append(full_path)
    
    if not available_files:
        print(f"{Fore.RED}No se encontraron archivos .txt en los directorios de entrada{Style.RESET_ALL}")
        return None
    
    available_files.sort()
    
    print(f"\n{Fore.CYAN}=== ARCHIVOS DE PRUEBA DISPONIBLES ==={Style.RESET_ALL}")
    print(f"{Fore.RED}\t Presione [q] para salir.{Style.RESET_ALL}")
    
    for i, file in enumerate(available_files, 1):
        print(f"{Fore.YELLOW}{i:2d}.{Style.RESET_ALL} {file}")
    
    while True:
        try:
            choice = input(f"\n{Fore.GREEN}Seleccione un archivo (1-{len(available_files)}): {Style.RESET_ALL}")
            if choice.lower() == 'q':
                return None
                
            choice_idx = int(choice) - 1
            if 0 <= choice_idx < len(available_files):
                return available_files[choice_idx]
            print(f"{Fore.RED}¡Selección inválida! Intente nuevamente.{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.RED}¡Ingrese un número válido!{Style.RESET_ALL}")

def show_main_menu():
    """Muestra el menú principal de opciones"""
    options = [
        "Ejecutar todo el flujo completo y compilar el binario con optimización (opt)",
        "Ejecutar todo el flujo completo y compilar el binario sin optimización",
        "Ejecutar todo el flujo completo y compilar un .exe optimizado para Windows",
        "Ejecutar únicamente hasta la generación de código intermedio .ll",
        "Tomar como entrada un .ll optimizado manualmente y compilar el binario",
        "Convertir el binario a .exe",
        "Salir"
    ]
    
    print(f"\n{Fore.CYAN}=== MENÚ PRINCIPAL ==={Style.RESET_ALL}")
    for i, option in enumerate(options, 1):
        print(f"{Fore.YELLOW}{i}.{Style.RESET_ALL} {option}")
    
    while True:
        try:
            choice = input(f"\n{Fore.GREEN}Seleccione una opción (1-{len(options)}): {Style.RESET_ALL}")
            choice_idx = int(choice)
            if 1 <= choice_idx <= len(options):
                return choice_idx
            print(f"{Fore.RED}¡Opción inválida! Intente nuevamente.{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.RED}¡Ingrese un número válido!{Style.RESET_ALL}")

def process_input_file(path_file, timer):
    """Procesa el archivo de entrada hasta generar el código LLVM"""
    if not check_extension(path_file):
        raise ValueError("El archivo debe tener extensión .txt")
    
    print_section("configuración inicial")
    print(f"{Fore.WHITE}Analizando archivo: {Fore.YELLOW}{path_file}{Style.RESET_ALL}")
    
    # ========== FASE 2: Análisis léxico ==========
    timer.start_phase("Análisis léxico")
    input_stream = FileStream(path_file, encoding='utf-8')
    lexer = ExprLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    timer.end_phase()
    
    # ========== FASE 3: Análisis sintáctico ==========
    timer.start_phase("Análisis sintáctico")
    parser = ExprParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(PersonalizatedListener())
    tree = parser.gramatica()
    timer.end_phase()
    
    # Visualización del árbol
    print_section("estructura del árbol", Fore.BLUE)
    pretty_print_tree(tree, parser)
    
    # ========== FASE 4: Ejecución del Listener ==========
    timer.start_phase("Ejecución del Listener")
    print_section("ejecución del listener", Fore.YELLOW)
    listener = PersonalizatedListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    timer.end_phase()
    
    # ========== FASE 5: Evaluación Visitor ==========
    timer.start_phase("Evaluación Visitor")
    print_section("evaluación visitor", Fore.MAGENTA)
    visitor = PersonalizatedVisitor()
    result = visitor.visit(tree)
    timer.end_phase()
    
    # ========== FASE 6: Generación AST ==========
    timer.start_phase("Generación AST")
    ast_visitor = ASTVisitor()
    ast_result = ast_visitor.visit(tree)
    timer.end_phase()
    
    print(f"\n{Fore.GREEN}✔ Análisis completado{Style.RESET_ALL}")
    success_logger.info(f"Análisis exitoso para {path_file}")
    print_section("AST generado", Fore.CYAN)
    print(ast_result)

    # ========== FASE 7: Generación LLVM ==========
    timer.start_phase("Generación LLVM")
    logging.info("Generando código LLVM...")
    llvm_generator = LLVMGenerator()
    llvm_code = llvm_generator.generate_code(ast_result)
    timer.end_phase()
    
    with open("outputs/output.ll", "w", encoding='utf-8') as f:
        f.write(str(llvm_code))
    print(f"IR generado y guardado en: outputs/output.ll")
    logging.info("Código LLVM generado:")
    print(str(llvm_code))
    
    return llvm_code

def main():
    print_banner()
    
    while True:
        # ========== FASE 1: Selección de archivo ==========
        timer = TimeMeasurer()
        timer.start_phase("Selección de archivo")
        path_file = show_file_menu()
        if not path_file:
            print(f"{Fore.YELLOW}Operación cancelada por el usuario.{Style.RESET_ALL}")
            break
        
        timer.end_phase()
        
        # Mostrar menú principal
        option = show_main_menu()
        
        try:
            if option == 1:  # Flujo completo con optimización
                llvm_code = process_input_file(path_file, timer)
                
                # ========== FASE 8: Compilación con optimización ==========
                timer.start_phase("Compilación con optimización")
                logging.info("Compilando con optimización...")
                if not compile_llvm_ir(llvm_code, optimize=True, generate_executable=True, run_program=False):
                    print(f"{Fore.RED}✖ Fallo en la compilación o ejecución{Style.RESET_ALL}")
                timer.end_phase()
                
                # Mostrar reporte de tiempos y suma sin selección de archivo
                timer.print_report()
                # Suma de tiempos excepto "Selección de archivo"
                total_sin_seleccion = sum(
                    tiempo for fase, tiempo in timer.phases.items() if fase != "Selección de archivo"
                )
                print(f"\n{Fore.MAGENTA}TOTAL (sin Selección de archivo): {total_sin_seleccion:.4f} segundos{Style.RESET_ALL}")
                
            elif option == 2:  # Flujo completo sin optimización
                llvm_code = process_input_file(path_file, timer)
                
                # ========== FASE 8: Compilación sin optimización ==========
                timer.start_phase("Compilación sin optimización")
                logging.info("Compilando sin optimización...")
                if not compile_llvm_ir(llvm_code, optimize=False, generate_executable=True, run_program=False):
                    print(f"{Fore.RED}✖ Fallo en la compilación o ejecución{Style.RESET_ALL}")
                timer.end_phase()
                
                timer.print_report()
                
            elif option == 3:  # Flujo completo con optimización para .exe
                llvm_code = process_input_file(path_file, timer)
                
                # ========== FASE 8: Compilación con optimización para Windows ==========
                timer.start_phase("Compilación para .exe optimizado")
                logging.info("Compilando .exe optimizado...")
                if not compile_llvm_ir(llvm_code, optimize=True, generate_executable=True, 
                                      run_program=False, target_exe=True):
                    print(f"{Fore.RED}✖ Fallo en la compilación o ejecución{Style.RESET_ALL}")
                timer.end_phase()
                
                timer.print_report()
                
            elif option == 4:  # Solo generación de LLVM
                llvm_code = process_input_file(path_file, timer)
                print(f"{Fore.GREEN}✔ Proceso completado hasta generación de LLVM{Style.RESET_ALL}")
                timer.print_report()
                
            elif option == 5:  # Compilar .ll existente
                ll_file = input(f"{Fore.GREEN}Ingrese la ruta del archivo .ll optimizado: {Style.RESET_ALL}")
                timer.start_phase("Compilación de .ll optimizado")
                if not compile_existing_llvm(ll_file, optimize=True):
                    print(f"{Fore.RED}✖ Fallo en la compilación{Style.RESET_ALL}")
                timer.end_phase()
                timer.print_report()
                
            elif option == 6:  # Convertir a .exe
                bin_file = input(f"{Fore.GREEN}Ingrese la ruta del binario a convertir: {Style.RESET_ALL}")
                timer.start_phase("Conversión a .exe")
                if not convert_to_exe(bin_file):
                    print(f"{Fore.RED}✖ Fallo en la conversión{Style.RESET_ALL}")
                timer.end_phase()
                timer.print_report()
                
            elif option == 7:  # Salir
                print(f"{Fore.YELLOW}Saliendo del programa...{Style.RESET_ALL}")
                break
                
        except FileNotFoundError as fnf_error:
            timer.end_phase()
            error_msg = f"{Fore.RED}✖ Archivo no encontrado: {fnf_error}{Style.RESET_ALL}"
            print(error_msg)
            error_logger.error(error_msg)
            timer.print_report()
        except ValueError as ve:
            timer.end_phase()
            error_msg = f"{Fore.RED}✖ Error de valor: {ve}{Style.RESET_ALL}"
            print(error_msg)
            error_logger.error(error_msg)
            timer.print_report()
        except Exception as e:
            timer.end_phase()
            error_msg = f"{Fore.RED}✖ Error inesperado: {str(e)}{Style.RESET_ALL}"
            print(error_msg)
            error_logger.error(error_msg)
            timer.print_report()
            raise

if __name__ == "__main__":
    main()