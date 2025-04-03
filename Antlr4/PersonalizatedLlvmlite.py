from llvmlite import ir
from llvmlite.ir import Constant, IRBuilder
import llvmlite.binding as llvm
from llvmlite.ir._utils import DuplicatedNameError  # Agrega esta importación
class LLVMGenerator:
    def __init__(self):
        # Initialize LLVM components
        self.module = ir.Module(name="main_module")
        self.module.triple = llvm.get_default_triple()
        
        self.builder = None
        self.functions = {}
        self.symbol_table = {}
        self.current_function = None
        # Add printf declaration for print statements
        voidptr_ty = ir.IntType(8).as_pointer()
        printf_ty = ir.FunctionType(ir.IntType(32), [voidptr_ty], var_arg=True)
        printf = ir.Function(self.module, printf_ty, name="printf")
        self.printf = printf
        
        # Add standard types
        self.type_map = {
            'entero': ir.IntType(32),
            'decimal': ir.DoubleType(),
            'bool': ir.IntType(1),
            'cadena': ir.IntType(8).as_pointer()
        }
    
    def generate_code(self, ast_node):
        # Create main function
        main_func_type = ir.FunctionType(ir.IntType(32), [])
        main_func = ir.Function(self.module, main_func_type, name="main")
        main_block = main_func.append_basic_block(name="entry")
        self.builder = IRBuilder(main_block)
        
        # Generate code for the main function body
        self.visit(ast_node)
        
        # Add return 0 at the end of main
        self.builder.ret(Constant(ir.IntType(32), 0))
        
        return self.module
    
    def visit(self, node):
        method_name = f'visit_{node.type}'
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)
    
    def generic_visit(self, node):
        for child in node.children:
            self.visit(child)
    
    def visit_Program(self, node):
        self.visit(node.children[0])
    
    def visit_MainFunction(self, node):
        for child in node.children:
            self.visit(child)
    
    def visit_Block(self, node):
        for stmt in node.children:
            self.visit(stmt)
    
    def visit_VariableDecl(self, node):
        var_name = node.value
        var_type = self.visit(node.children[0])
        value = self.visit(node.children[1]) if len(node.children) > 1 else None
        
        # Allocate space for the variable
        ptr = self.builder.alloca(var_type, name=var_name)
        self.symbol_table[var_name] = ptr
        
        # Store initial value if exists
        if value is not None:
            self.builder.store(value, ptr)
    
    def visit_Type(self, node):
        return self.type_map[node.value]
    
    def visit_Literal(self, node):
        if isinstance(node.value, bool):
            return Constant(ir.IntType(1), int(node.value))
        elif isinstance(node.value, int):
            return Constant(ir.IntType(32), node.value)
        elif isinstance(node.value, float):
            return Constant(ir.DoubleType(), node.value)
        elif isinstance(node.value, str):
            # Create global string constant
            str_val = bytearray((node.value + '\00').encode('utf-8'))
            str_const = ir.Constant(ir.ArrayType(ir.IntType(8), len(str_val)), str_val)
            global_str = ir.GlobalVariable(
                self.module, 
                str_const.type, 
                name=f"str.{len(self.module.global_values)}"
            )
            global_str.linkage = 'internal'
            global_str.global_constant = True
            global_str.initializer = str_const
            
            # Get pointer to the string
            zero = Constant(ir.IntType(32), 0)
            return self.builder.gep(global_str, [zero, zero], name=f"strptr.{len(self.module.global_values)}")
    
    def visit_Variable(self, node):
        var_name = node.value
        if var_name not in self.symbol_table:
            raise NameError(f"Variable '{var_name}' not defined")
        ptr = self.symbol_table[var_name]
        return self.builder.load(ptr, name=var_name)
    
    def visit_Assignment(self, node):
        var_name = node.value
        value = self.visit(node.children[0])
        
        if var_name not in self.symbol_table:
            raise NameError(f"Variable '{var_name}' not defined")
        
        ptr = self.symbol_table[var_name]
        self.builder.store(value, ptr)
        return value
    
    def visit_BinaryOp(self, node):
        left = self.visit(node.children[0])
        right = self.visit(node.children[1])
        
        op = node.value
        
        if op in ('+', '-', '*', '/'):
            if isinstance(left.type, ir.IntType) and isinstance(right.type, ir.IntType):
                if op == '+':
                    return self.builder.add(left, right, name="addtmp")
                elif op == '-':
                    return self.builder.sub(left, right, name="subtmp")
                elif op == '*':
                    return self.builder.mul(left, right, name="multmp")
                elif op == '/':
                    return self.builder.sdiv(left, right, name="divtmp")
            elif isinstance(left.type, ir.DoubleType) or isinstance(right.type, ir.DoubleType):
                # Promote integers to doubles if needed
                if isinstance(left.type, ir.IntType):
                    left = self.builder.sitofp(left, ir.DoubleType(), name="sitofp")
                if isinstance(right.type, ir.IntType):
                    right = self.builder.sitofp(right, ir.DoubleType(), name="sitofp")
                
                if op == '+':
                    return self.builder.fadd(left, right, name="faddtmp")
                elif op == '-':
                    return self.builder.fsub(left, right, name="fsubtmp")
                elif op == '*':
                    return self.builder.fmul(left, right, name="fmultmp")
                elif op == '/':
                    return self.builder.fdiv(left, right, name="fdivtmp")
        
        elif op in ('<', '>', '<=', '>=', '==', '!='):
            if isinstance(left.type, ir.IntType) and isinstance(right.type, ir.IntType):
                if op == '<':
                    return self.builder.icmp_signed('<', left, right, name="cmptmp")
                elif op == '<=':
                    return self.builder.icmp_signed('<=', left, right, name="cmptmp")
                elif op == '>':
                    return self.builder.icmp_signed('>', left, right, name="cmptmp")
                elif op == '>=':
                    return self.builder.icmp_signed('>=', left, right, name="cmptmp")
                elif op == '==':
                    return self.builder.icmp_signed('==', left, right, name="cmptmp")
                elif op == '!=':
                    return self.builder.icmp_signed('!=', left, right, name="cmptmp")
            elif isinstance(left.type, ir.DoubleType) or isinstance(right.type, ir.DoubleType):
                if op == '<':
                    return self.builder.fcmp_ordered('<', left, right, name="cmptmp")
                elif op == '<=':
                    return self.builder.fcmp_ordered('<=', left, right, name="cmptmp")
                elif op == '>':
                    return self.builder.fcmp_ordered('>', left, right, name="cmptmp")
                elif op == '>=':
                    return self.builder.fcmp_ordered('>=', left, right, name="cmptmp")
                elif op == '==':
                    return self.builder.fcmp_ordered('==', left, right, name="cmptmp")
                elif op == '!=':
                    return self.builder.fcmp_ordered('!=', left, right, name="cmptmp")
        
        raise ValueError(f"Unknown binary operator: {op}")
    
    def visit_UnaryOp(self, node):
        operand = self.visit(node.children[0])
        op = node.value
        
        if op == '-':
            if isinstance(operand.type, ir.IntType):
                return self.builder.neg(operand, name="negtmp")
            elif isinstance(operand.type, ir.DoubleType):
                return self.builder.fneg(operand, name="fnegtmp")
        elif op == '++':
            # Increment operation
            one = Constant(operand.type, 1)
            new_val = self.builder.add(operand, one, name="incrtmp")
            self.builder.store(new_val, self.symbol_table[node.children[0].value])
            return new_val
        elif op == '--':
            # Decrement operation
            one = Constant(operand.type, 1)
            new_val = self.builder.sub(operand, one, name="decrtmp")
            self.builder.store(new_val, self.symbol_table[node.children[0].value])
            return new_val
        
        raise ValueError(f"Unknown unary operator: {op}")
    
    def visit_PrintStatement(self, node):
        value = self.visit(node.children[0])
        
        # Determine format string based on type
        if isinstance(value.type, ir.IntType) and value.type.width == 32:
            fmt_str = "%d\n\00"
        elif isinstance(value.type, ir.DoubleType):
            fmt_str = "%f\n\00"
        elif isinstance(value.type, ir.IntType) and value.type.width == 1:
            fmt_str = "%s\n\00"
            # Convert bool to string
            true_str = "true\00"
            false_str = "false\00"
            
            true_const = ir.Constant(ir.ArrayType(ir.IntType(8), len(true_str)), bytearray(true_str.encode('utf-8')))
            false_const = ir.Constant(ir.ArrayType(ir.IntType(8), len(false_str)), bytearray(false_str.encode('utf-8')))
            
            true_global = ir.GlobalVariable(self.module, true_const.type, name=f"true_str.{len(self.module.global_values)}")
            true_global.linkage = 'internal'
            true_global.global_constant = True
            true_global.initializer = true_const
            
            false_global = ir.GlobalVariable(self.module, false_const.type, name=f"false_str.{len(self.module.global_values)}")
            false_global.linkage = 'internal'
            false_global.global_constant = True
            false_global.initializer = false_const
            
            zero = Constant(ir.IntType(32), 0)
            true_ptr = self.builder.gep(true_global, [zero, zero], name="trueptr")
            false_ptr = self.builder.gep(false_global, [zero, zero], name="falseptr")
            
            value = self.builder.select(value, true_ptr, false_ptr, name="boolstr")
        elif isinstance(value.type, ir.PointerType) and isinstance(value.type.pointee, ir.IntType) and value.type.pointee.width == 8:
            fmt_str = "%s\n\00"
        else:
            raise ValueError(f"Unsupported type for print: {value.type}")
        
        # Create format string constant
        fmt_const = ir.Constant(ir.ArrayType(ir.IntType(8), len(fmt_str)), bytearray(fmt_str.encode('utf-8')))
        fmt_global = ir.GlobalVariable(self.module, fmt_const.type, name=f"fmt.{len(self.module.global_values)}")
        fmt_global.linkage = 'internal'
        fmt_global.global_constant = True
        fmt_global.initializer = fmt_const
        
        zero = Constant(ir.IntType(32), 0)
        fmt_ptr = self.builder.gep(fmt_global, [zero, zero], name="fmtptr")
        
        # Call printf
        self.builder.call(self.printf, [fmt_ptr, value])
    
    def visit_IfStatement(self, node):
        conditions = node.children[0].children
        blocks = node.children[1].children
        else_block = node.children[2] if len(node.children) > 2 else None
        
        # Create basic blocks
        current_block = self.builder.block
        func = current_block.parent
        
        # Store references to else blocks we create
        else_blocks = []
        
        # Handle all if/else if blocks
        for i, (cond, block) in enumerate(zip(conditions, blocks)):
            # Create blocks
            then_block = func.append_basic_block(f"then.{i}")
            merge_block = func.append_basic_block(f"ifcont.{i}")
            
            # Create else block if needed
            if i < len(conditions)-1 or else_block:
                else_block_bb = func.append_basic_block(f"else.{i}")
                else_blocks.append(else_block_bb)
            
            # Generate condition
            cond_val = self.visit(cond)
            
            # If this isn't the first condition, we need to branch from the previous else block
            if i > 0:
                self.builder.branch(then_block)
            
            # Set insert point to current block for the condition
            self.builder.position_at_end(current_block)
            self.builder.cbranch(
                cond_val, 
                then_block, 
                merge_block if i == len(conditions)-1 and not else_block else else_blocks[i]
            )
            
            # Generate then block
            self.builder.position_at_end(then_block)
            self.visit(block)
            self.builder.branch(merge_block)
            
            # Next condition starts at the else block
            if i < len(conditions)-1 or else_block:
                current_block = else_blocks[i]
            else:
                current_block = merge_block
        
        # Handle else block if exists
        if else_block:
            else_block_bb = func.append_basic_block("else")
            self.builder.position_at_end(current_block)
            self.builder.branch(else_block_bb)
            
            self.builder.position_at_end(else_block_bb)
            self.visit(else_block)
            self.builder.branch(merge_block)
        
        # Set insert point to merge block
        if len(conditions) > 0 or else_block:
            self.builder.position_at_end(merge_block)
    
    def visit_WhileLoop(self, node):
        cond = node.children[0]
        body = node.children[1]
        
        func = self.builder.block.parent
        cond_block = func.append_basic_block("while.cond")
        body_block = func.append_basic_block("while.body")
        end_block = func.append_basic_block("while.end")
        
        # Branch to condition block
        self.builder.branch(cond_block)
        
        # Generate condition
        self.builder.position_at_end(cond_block)
        cond_val = self.visit(cond)
        self.builder.cbranch(cond_val, body_block, end_block)
        
        # Generate body
        self.builder.position_at_end(body_block)
        self.visit(body)
        self.builder.branch(cond_block)  # Loop back to condition
        
        # Continue after loop
        self.builder.position_at_end(end_block)
    
    def visit_ForLoop(self, node):
        init = node.children[0]
        cond = node.children[1]
        update = node.children[2]
        body = node.children[3]
        
        # Generate initialization
        self.visit(init)
        
        func = self.builder.block.parent
        cond_block = func.append_basic_block("for.cond")
        body_block = func.append_basic_block("for.body")
        update_block = func.append_basic_block("for.update")
        end_block = func.append_basic_block("for.end")
        
        # Branch to condition block
        self.builder.branch(cond_block)
        
        # Generate condition
        self.builder.position_at_end(cond_block)
        cond_val = self.visit(cond)
        self.builder.cbranch(cond_val, body_block, end_block)
        
        # Generate body
        self.builder.position_at_end(body_block)
        self.visit(body)
        self.builder.branch(update_block)
        
        # Generate update
        self.builder.position_at_end(update_block)
        self.visit(update)
        self.builder.branch(cond_block)  # Loop back to condition
        
        # Continue after loop
        self.builder.position_at_end(end_block)
    
    def visit_FunctionDecl(self, node):
        func_name = node.value
        return_type = self.visit(node.children[0])
        params = node.children[1].children
        
        # Create parameter types
        param_types = []
        for param in params:
            param_type = self.visit(param.children[0])
            param_types.append(param_type)
        
        # Create function type
        func_type = ir.FunctionType(return_type, param_types)
        func = ir.Function(self.module, func_type, name=func_name)
        self.functions[func_name] = func
        
        # Create entry block
        entry_block = func.append_basic_block(name="entry")
        self.builder = IRBuilder(entry_block)
        
        # Store parameters in symbol table
        for i, param in enumerate(params):
            param_name = param.value
            param_var = func.args[i]
            param_var.name = param_name
            
            # Allocate space for parameter
            ptr = self.builder.alloca(param_types[i], name=param_name)
            self.builder.store(param_var, ptr)
            self.symbol_table[param_name] = ptr
        
        # Generate function body
        self.visit(node.children[2])
        
        # Generate return statement
        ret_val = self.visit(node.children[3])
        self.builder.ret(ret_val)
        
        # Reset builder to main function
        main_func = self.module.get_global('main')
        if main_func:
            # Instead of creating an empty block, return to the main block
            self.builder.position_at_end(main_func.entry_basic_block)
        else:
            # If no main function exists, just create a new builder without adding it to the module
            self.builder = IRBuilder(ir.Block(self.module.context, "dummy_block"))
            
    def visit_FunctionCall(self, node):
        func_name = node.value
        args = [self.visit(arg) for arg in node.children]
        
        if func_name not in self.functions:
            raise NameError(f"Function '{func_name}' not defined")
        
        func = self.functions[func_name]
        return self.builder.call(func, args, name=f"call.{func_name}")
    
    def visit_Parameter(self, node):
        # Parameters are handled in FunctionDecl visitor
        pass
    
    def save_to_file(self, llvm_module, filename="output.ll"):
        with open(filename, "w") as f:
            f.write(str(llvm_module))