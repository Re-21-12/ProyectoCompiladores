from llvmlite import ir

# Crear un módulo LLVM
module = ir.Module(name="simple_module")

# Crear un contexto y un tipo de función
function_type = ir.FunctionType(ir.IntType(32), [])
function = ir.Function(module, function_type, name="main")

# Crear un bloque de instrucciones dentro de la función
block = function.append_basic_block(name="entry")
builder = ir.IRBuilder(block)
    