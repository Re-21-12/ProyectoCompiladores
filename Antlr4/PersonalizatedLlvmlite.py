from llvmlite import ir
from llvmlite.ir import Constant, IRBuilder
import llvmlite.binding as llvm

class LLVMGenerator:
    def __init__(self):
        # Initialize LLVM
        llvm.initialize()
        llvm.initialize_native_target()
        llvm.initialize_native_asmprinter()
        
        # Create module
        self.module = ir.Module(name="main_module")
        self.module.triple = llvm.get_process_triple()
        target = llvm.Target.from_triple(self.module.triple)
        self.module.data_layout = target.create_target_machine().target_data
        
        # Initialize builder and context
        self.builder = None
        self.current_function = None
        
        # Symbol tables
        self.functions = {}
        self.symbol_table = {}
        self.string_constants = {}
        
        # Type definitions
        self.int_type = ir.IntType(32)       # entero
        self.double_type = ir.DoubleType()   # decimal
        self.bool_type = ir.IntType(1)       # bool
        self.void_type = ir.VoidType()       # void
        self.char_ptr_type = ir.IntType(8).as_pointer()  # cadena
        
        # Initialize builtins
        self._declare_builtins()

    def _declare_builtins(self):
        """Declare built-in functions like printf"""
        printf_type = ir.FunctionType(self.int_type, [self.char_ptr_type], var_arg=True)
        ir.Function(self.module, printf_type, name="printf")

    def generate_code(self, ast_node):
        """Generate LLVM IR from AST"""
        # Create main function
        main_func_type = ir.FunctionType(self.int_type, [])
        main_func = ir.Function(self.module, main_func_type, name="main")
        self.current_function = main_func
        
        # Create entry block
        entry_block = main_func.append_basic_block(name="entry")
        self.builder = IRBuilder(entry_block)
        
        # Generate code for the AST
        self._generate_node(ast_node)
        
        # Ensure main has a return
        if not entry_block.is_terminated:
            self.builder.ret(Constant(self.int_type, 0))
        
        return self.module

    def _generate_node(self, node):
        """Dispatch node generation based on type"""
        node_type = node.type
        
        if node_type == "Program":
            for child in node.children:
                self._generate_node(child)
                
        elif node_type == "MainFunction":
            for child in node.children:
                self._generate_node(child)
                
        elif node_type == "Block":
            for child in node.children:
                self._generate_node(child)
                
        elif node_type == "VariableDecl":
            self._generate_variable_decl(node)
                
        elif node_type == "Assignment":
            self._generate_assignment(node)
            
        elif node_type == "PrintStatement":
            self._generate_print(node.children[0])
            
        elif node_type == "IfStatement":
            self._generate_if_statement(node)
            
        elif node_type == "WhileLoop":
            self._generate_while_loop(node)
            
        elif node_type == "ForLoop":
            self._generate_for_loop(node)
            
        elif node_type == "FunctionDecl":
            self._generate_function_decl(node)
            
        elif node_type == "FunctionCall":
            return self._generate_function_call(node)
            
        elif node_type == "ReturnStatement":
            self._generate_return(node)

    def _generate_variable_decl(self, node):
        """Generate variable declaration"""
        var_name = node.value
        var_type = self._llvm_type(node.children[0].value)
        
        # Allocate space on stack
        ptr = self.builder.alloca(var_type, name=var_name)
        self.symbol_table[var_name] = ptr
        
        # Initialize if needed
        if len(node.children) > 1:
            value = self._generate_expression(node.children[1])
            self.builder.store(value, ptr)

    def _generate_assignment(self, node):
        """Generate variable assignment"""
        var_name = node.value
        ptr = self.symbol_table[var_name]
        value = self._generate_expression(node.children[0])
        self.builder.store(value, ptr)

    def _generate_print(self, expr_node):
        """Generate print statement"""
        value = self._generate_expression(expr_node)
        value_type = self._get_expression_type(expr_node)
        
        # Get printf function
        printf = self.module.get_global("printf")
        
        # Create format string based on type
        if isinstance(value_type, ir.IntType) and value_type.width == 32:
            fmt_str = "%d\n\0"
        elif isinstance(value_type, ir.DoubleType):
            fmt_str = "%f\n\0"
        elif isinstance(value_type, ir.IntType) and value_type.width == 1:  # bool
            fmt_str = "%d\n\0"
        else:  # string
            fmt_str = "%s\n\0"
        
        # Create global constant for format string
        if fmt_str not in self.string_constants:
            byte_array = bytearray(fmt_str.encode("utf8"))
            fmt = ir.Constant(ir.ArrayType(ir.IntType(8), len(byte_array)), byte_array)
            global_fmt = ir.GlobalVariable(self.module, fmt.type, name=f"fmt.{len(self.string_constants)}")
            global_fmt.linkage = "internal"
            global_fmt.global_constant = True
            global_fmt.initializer = fmt
            self.string_constants[fmt_str] = global_fmt
        
        # Get pointer to format string
        fmt_ptr = self.builder.bitcast(self.string_constants[fmt_str], self.char_ptr_type)
        
        # Call printf
        if isinstance(value_type, ir.IntType) and value_type.width == 1:  # bool
            value = self.builder.zext(value, self.int_type)
        self.builder.call(printf, [fmt_ptr, value])

    def _generate_if_statement(self, node):
        """Generate if-else statement"""
        # Get condition, then block, and optional else block
        condition = node.children[0]
        then_block_node = node.children[1]
        else_block_node = node.children[2] if len(node.children) > 2 else None
        
        # Create basic blocks
        then_block = self.builder.append_basic_block("if.then")
        end_block = self.builder.append_basic_block("if.end")
        else_block = self.builder.append_basic_block("if.else") if else_block_node else end_block
        
        # Generate condition and branch
        cond_value = self._generate_expression(condition)
        self.builder.cbranch(cond_value, then_block, else_block)
        
        # Generate then block
        self.builder.position_at_end(then_block)
        self._generate_node(then_block_node)
        if not self.builder.block.is_terminated:
            self.builder.branch(end_block)
        
        # Generate else block if exists
        if else_block_node and else_block != end_block:
            self.builder.position_at_end(else_block)
            self._generate_node(else_block_node)
            if not self.builder.block.is_terminated:
                self.builder.branch(end_block)
        
        # Continue after if
        self.builder.position_at_end(end_block)

    def _generate_while_loop(self, node):
        """Generate while loop"""
        condition = node.children[0]
        body = node.children[1]
        
        # Create basic blocks
        cond_block = self.builder.append_basic_block("while.cond")
        body_block = self.builder.append_basic_block("while.body")
        end_block = self.builder.append_basic_block("while.end")
        
        # Jump to condition
        self.builder.branch(cond_block)
        
        # Generate condition
        self.builder.position_at_end(cond_block)
        cond_value = self._generate_expression(condition)
        self.builder.cbranch(cond_value, body_block, end_block)
        
        # Generate body
        self.builder.position_at_end(body_block)
        self._generate_node(body)
        if not self.builder.block.is_terminated:
            self.builder.branch(cond_block)  # Loop back
        
        # Continue after while
        self.builder.position_at_end(end_block)

    def _generate_for_loop(self, node):
        """Generate for loop"""
        init, cond, update, body = node.children
        
        # Create basic blocks
        cond_block = self.builder.append_basic_block("for.cond")
        body_block = self.builder.append_basic_block("for.body")
        update_block = self.builder.append_basic_block("for.update")
        end_block = self.builder.append_basic_block("for.end")
        
        # Generate initialization
        self._generate_node(init)
        self.builder.branch(cond_block)
        
        # Generate condition
        self.builder.position_at_end(cond_block)
        cond_value = self._generate_expression(cond)
        self.builder.cbranch(cond_value, body_block, end_block)
        
        # Generate body
        self.builder.position_at_end(body_block)
        self._generate_node(body)
        if not self.builder.block.is_terminated:
            self.builder.branch(update_block)
        
        # Generate update
        self.builder.position_at_end(update_block)
        self._generate_node(update)
        if not self.builder.block.is_terminated:
            self.builder.branch(cond_block)  # Loop back
        
        # Continue after for
        self.builder.position_at_end(end_block)

    def _generate_function_decl(self, node):
        """Generate function declaration"""
        func_name = node.value
        return_type = self._llvm_type(node.children[0].value)
        params = node.children[1].children
        body_node = node.children[2]
        
        # Create parameter types
        param_types = [self._llvm_type(p.children[0].value) for p in params]
        func_type = ir.FunctionType(return_type, param_types)
        
        # Create function
        func = ir.Function(self.module, func_type, name=func_name)
        
        # Save current context
        old_function = self.current_function
        old_symbol_table = self.symbol_table.copy()
        
        # Set new context
        self.current_function = func
        self.symbol_table = {}
        entry_block = func.append_basic_block("entry")
        self.builder = IRBuilder(entry_block)
        
        # Store parameters
        for i, (param, param_node) in enumerate(zip(func.args, params)):
            param_name = param_node.value
            ptr = self.builder.alloca(param.type, name=f"{param_name}.addr")
            self.builder.store(param, ptr)
            self.symbol_table[param_name] = ptr
        
        # Generate body
        self._generate_node(body_node)
        
        # Ensure return if needed
        if not entry_block.is_terminated:
            if return_type == self.void_type:
                self.builder.ret_void()
            else:
                self.builder.ret(Constant(return_type, 0))
        
        # Restore context
        self.current_function = old_function
        self.symbol_table = old_symbol_table
        
        # Register function
        self.functions[func_name] = {
            "function": func,
            "return_type": return_type,
            "param_types": param_types
        }

    def _generate_function_call(self, node):
        """Generate function call"""
        func_name = node.value
        args = [self._generate_expression(arg) for arg in node.children]
        
        # Look up function
        if func_name in self.functions:
            func = self.functions[func_name]["function"]
            return self.builder.call(func, args)
        else:
            raise Exception(f"Function '{func_name}' not declared")

    def _generate_return(self, node):
        """Generate return statement"""
        if len(node.children) > 0:
            ret_value = self._generate_expression(node.children[0])
            self.builder.ret(ret_value)
        else:
            self.builder.ret_void()

    def _generate_expression(self, node):
        """Generate expression code"""
        if node.type == "Literal":
            return self._generate_literal(node)
        elif node.type == "Variable":
            return self._generate_variable(node)
        elif node.type == "BinaryOp":
            return self._generate_binary_op(node)
        elif node.type == "UnaryOp":
            return self._generate_unary_op(node)
        elif node.type == "FunctionCall":
            return self._generate_function_call(node)
        else:
            return Constant(self.int_type, 0)  # Default value

    def _generate_literal(self, node):
        """Generate literal value"""
        if isinstance(node.value, bool):
            return Constant(self.bool_type, int(node.value))
        elif isinstance(node.value, int):
            return Constant(self.int_type, node.value)
        elif isinstance(node.value, float):
            return Constant(self.double_type, node.value)
        elif isinstance(node.value, str):
            return self._generate_string(node.value)
        else:
            return Constant(self.int_type, 0)

    def _generate_string(self, value):
        """Generate string constant"""
        # Create global constant for string
        str_type = ir.ArrayType(ir.IntType(8), len(value) + 1)
        str_const = ir.Constant(str_type, bytearray(value.encode('utf-8') + b'\x00'))
        
        # Create global variable
        global_str = ir.GlobalVariable(self.module, str_type, name=f"str.{len(self.string_constants)}")
        global_str.linkage = "internal"
        global_str.global_constant = True
        global_str.initializer = str_const
        self.string_constants[value] = global_str
        
        # Get pointer to first character
        zero = Constant(ir.IntType(32), 0)
        return self.builder.gep(global_str, [zero, zero], name="strptr")

    def _generate_variable(self, node):
        """Generate variable access"""
        var_name = node.value
        ptr = self.symbol_table[var_name]
        return self.builder.load(ptr, name=f"{var_name}.val")

    def _generate_binary_op(self, node):
        """Generate binary operation"""
        left = self._generate_expression(node.children[0])
        right = self._generate_expression(node.children[1])
        op = node.value
        
        # Determine types
        left_type = self._get_expression_type(node.children[0])
        right_type = self._get_expression_type(node.children[1])
        
        # Convert types if needed
        if left_type != right_type:
            if isinstance(left_type, ir.IntType) and isinstance(right_type, ir.DoubleType):
                left = self.builder.sitofp(left, self.double_type)
            elif isinstance(left_type, ir.DoubleType) and isinstance(right_type, ir.IntType):
                right = self.builder.sitofp(right, self.double_type)
        
        # Perform operation
        if op in ["+", "-", "*", "/"]:
            if isinstance(left_type, ir.DoubleType) or isinstance(right_type, ir.DoubleType):
                if op == "+": return self.builder.fadd(left, right)
                elif op == "-": return self.builder.fsub(left, right)
                elif op == "*": return self.builder.fmul(left, right)
                else: return self.builder.fdiv(left, right)
            else:
                if op == "+": return self.builder.add(left, right)
                elif op == "-": return self.builder.sub(left, right)
                elif op == "*": return self.builder.mul(left, right)
                else: return self.builder.sdiv(left, right)
        elif op in ["<", ">", "<=", ">=", "==", "!="]:
            if isinstance(left_type, ir.DoubleType) or isinstance(right_type, ir.DoubleType):
                if op == "<": return self.builder.fcmp_ordered("<", left, right)
                elif op == ">": return self.builder.fcmp_ordered(">", left, right)
                elif op == "<=": return self.builder.fcmp_ordered("<=", left, right)
                elif op == ">=": return self.builder.fcmp_ordered(">=", left, right)
                elif op == "==": return self.builder.fcmp_ordered("==", left, right)
                else: return self.builder.fcmp_ordered("!=", left, right)
            else:
                if op == "<": return self.builder.icmp_signed("<", left, right)
                elif op == ">": return self.builder.icmp_signed(">", left, right)
                elif op == "<=": return self.builder.icmp_signed("<=", left, right)
                elif op == ">=": return self.builder.icmp_signed(">=", left, right)
                elif op == "==": return self.builder.icmp_signed("==", left, right)
                else: return self.builder.icmp_signed("!=", left, right)

    def _generate_unary_op(self, node):
        """Generate unary operation"""
        operand = self._generate_expression(node.children[0])
        op = node.value
        
        if op == "-":
            if isinstance(operand.type, ir.DoubleType):
                return self.builder.fneg(operand)
            else:
                return self.builder.sub(Constant(operand.type, 0), operand)
        elif op in ["++", "--"]:
            # Handle increment/decrement
            var_name = node.children[0].value
            ptr = self.symbol_table[var_name]
            value = self.builder.load(ptr)
            
            if isinstance(value.type, ir.DoubleType):
                delta = Constant(value.type, 1.0 if op == "++" else -1.0)
                new_value = self.builder.fadd(value, delta)
            else:
                delta = Constant(value.type, 1 if op == "++" else -1)
                new_value = self.builder.add(value, delta)
            
            self.builder.store(new_value, ptr)
            return new_value

    def _llvm_type(self, type_str):
        """Map language type to LLVM type"""
        type_map = {
            "entero": self.int_type,
            "decimal": self.double_type,
            "cadena": self.char_ptr_type,
            "bool": self.bool_type,
            "void": self.void_type
        }
        return type_map.get(type_str, self.int_type)

    def _get_expression_type(self, node):
        """Get LLVM type of an expression"""
        if node.type == "Literal":
            if isinstance(node.value, bool):
                return self.bool_type
            elif isinstance(node.value, int):
                return self.int_type
            elif isinstance(node.value, float):
                return self.double_type
            elif isinstance(node.value, str):
                return self.char_ptr_type
        elif node.type == "Variable":
            ptr = self.symbol_table[node.value]
            return ptr.type.pointee
        elif node.type == "BinaryOp":
            left_type = self._get_expression_type(node.children[0])
            right_type = self._get_expression_type(node.children[1])
            
            if node.value in ["+", "-", "*", "/"]:
                if isinstance(left_type, ir.DoubleType) or isinstance(right_type, ir.DoubleType):
                    return self.double_type
                return self.int_type
            else:
                return self.bool_type
        elif node.type == "UnaryOp":
            return self._get_expression_type(node.children[0])
        elif node.type == "FunctionCall":
            if node.value in self.functions:
                return self.functions[node.value]["return_type"]
            return self.int_type
        
        return self.int_type

    def save_to_file(self, filename="output.ll"):
        """Save generated IR to file"""
        llvm_ir = str(self.module)
        with open(filename, 'w') as f:
            f.write(llvm_ir)
        print(f"LLVM IR saved to {filename}")