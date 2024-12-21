#https://www.codewars.com/kata/5265b0885fda8eac5900093b/train/python

import re
import operator

class Compiler(object):
    
    operations = {
        "+" : operator.add,
        "-" : operator.sub,
        "*" : operator.mul,
        "/" : operator.floordiv
    }
    asm_operations = {
        "+" : "AD",
        "-" : "SU",
        "*" : "MU",
        "/" : "DI"
    }
    
    def compile(self, program):
        return self.pass3(self.pass2(self.pass1(program)))
        
    def tokenize(self, program):
        """Turn a program string into an array of tokens.  Each token
           is either '[', ']', '(', ')', '+', '-', '*', '/', a variable
           name or a number (as a string)"""
        token_iter = (m.group(0) for m in re.finditer(r'[-+*/()[\]]|[A-Za-z]+|\d+', program))
        return [int(tok) if tok.isdigit() else tok for tok in token_iter]

    def find_vars(self, tokens):
        for i in range(0, len(tokens)):
            if tokens[i] == "]":
                return [str(token) for token in tokens[1:i]], i
        raise Exception("Couldnt find Vars")
    
    def find_subprograms_parens(self, tokens, operators):
        balance = 0
        programs = []
        vars, vars_index = self.find_vars(tokens)
        for i in range(0, len(tokens)):
            if tokens[i] == "(":
                balance +=1
            elif tokens[i] == ")":
                balance -=1
            elif tokens[i] in operators and balance == 0:
                operation = tokens[i]
                programs.append("".join([str(token) for token in tokens[vars_index+1:i]]).lstrip("(").rstrip(")"))
                programs.append("".join([str(token) for token in tokens[i+1:]]).lstrip("(").rstrip(")"))
                break
        else:
            raise Exception("Couldnt find the operator to split the trees with, we dun goofed goofy")
        return programs, operation, vars, vars_index
    
    def find_subprograms_noparens(self, tokens):
        nonpriority_operators = ["+", "-"]
        priority_operators = ["*", "/"]
        programs = []
        
        vars, vars_index = self.find_vars(tokens)
        for i in range(len(tokens)-1, 0, -1):
            if tokens[i] in nonpriority_operators:
                operation = tokens[i]
                programs.append("".join([str(token) for token in tokens[vars_index+1:i]]))
                programs.append("".join([str(token) for token in tokens[i+1:]]))
                break
        else:
            for i in range(len(tokens)-1, 0, -1):
                if tokens[i] in priority_operators:
                    operation = tokens[i]
                    programs.append("".join([str(token) for token in tokens[vars_index+1:i]]))
                    programs.append("".join([str(token) for token in tokens[i+1:]]))
                    break
            else:
                raise Exception("Couldnt find the operator to split the trees with, we dun goofed goofy")                    
        return programs, operation, vars, vars_index
    
    def build_subprograms(self, programs, vars, var_index, operators):
        for x in range(0, len(programs)):
            program_vars = []
            for var in vars:
                if var in programs[x]:
                    program_vars.append(var)
            if program_vars == []:
                if not any([i in operators for i in programs[x]]):
                    programs[x] = "[] " + programs[x]
            elif len(program_vars) == 1:
                if "".join(program_vars) == programs[x]:
                    programs[x] = "[" + program_vars[0] + "" + str(vars.index(programs[x])) + "] " + programs[x]
            if not programs[x].startswith("["):
                programs[x] = "[" + " ".join(vars) + "] " + programs[x]
        return programs[0], programs[1]
        
    def find_subprograms(self, tokens, recursion_level = 0):
        operators = ["+", "-", "*", "/"]
        if "(" in tokens:
            programs, operation, vars, var_index = self.find_subprograms_parens(tokens, operators)
        else:
            programs, operation, vars, var_index = self.find_subprograms_noparens(tokens)
        left, right = self.build_subprograms(programs, vars, var_index, operators)
        print("\t"*recursion_level,"Left ->", left)
        print("\t"*recursion_level,"Right ->", right)
        print("\t"*recursion_level,"Operation ->", operation)
        return left, operation, right
                
    def pass1(self, program, recursion_level = 0):
        """Returns an un-optimized AST"""
        tokens = self.tokenize(program)
        print()
        print("%sFunc - Pass1::Recusion Level - %s || Program - %s || tokens - %s" % ("\t"*recursion_level, recursion_level, program, tokens))
        if program.startswith("[]"):
            return {'op' : 'imm', 'n' : tokens[-1]}
        elif re.findall(r'\[\w+\d+\]', program):
            return {'op' : 'arg', 'n' : tokens[2]}
        else:
            left, operation, right = self.find_subprograms(tokens, recursion_level = recursion_level)
            return {'op' : operation, 'a' : self.pass1(left, recursion_level = recursion_level + 1), 'b' : self.pass1(right, recursion_level = recursion_level + 1)}
        
    def pass2(self, ast, recursion_level = 0):
        """Returns an AST with constant expressions reduced"""
        print()
        print("%sFunc - Pass2::Recusion Level - %s || ast - %s" % ("\t"*recursion_level, recursion_level, ast))
        if ast.get("a", None) is None and ast.get("b", None) is None:
            return ast
        elif ast.get("a").get("op") == 'arg' and ast.get("b").get("op") == "arg":
            return ast
        elif ast.get("a").get("op") == 'imm' and ast.get("b").get("op") == 'imm':
            return {'op' : 'imm', 'n' : self.operations.get(ast.get("op"))(ast.get("a").get("n"), ast.get("b").get("n"))}
        elif ast.get("a").get("op") == 'arg' and ast.get("b").get("op") in list(self.operations.keys()):
            return {"op" : ast.get("op"), "a" : ast.get("a"), "b" : self.pass2(ast.get("b"), recursion_level = recursion_level+1)}
        elif ast.get("a").get("op") in  list(self.operations.keys()) and ast.get("b").get("op") == 'arg':
            return {"op" : ast.get("op"), "a" : self.pass2(ast.get("a"), recursion_level = recursion_level+1), "b" : ast.get("b")}
        else:
            ast = {"op" : ast.get("op"), "a" : self.pass2(ast.get("a"), recursion_level = recursion_level+1), "b" : self.pass2(ast.get("b"), recursion_level = recursion_level +1)}
            if ast.get("a").get("op") == 'imm' and ast.get("b").get("op") == 'imm':
                ast = {"op" : 'imm', 'n' : self.operations.get(ast.get("op"))(ast.get("a").get("n"), ast.get("b").get("n"))}
            if recursion_level == 0:
                print("Final Tree %s" % ast)
            return ast

    def pass3(self, ast, recursion_level = 0):
        """Returns assembly instructions"""
        print()
        print("%sFunc - Pass3::Recusion Level - %s || ast - %s " % ("\t"*recursion_level, recursion_level, ast))
        if ast.get("op") == "imm":
            print("%s %s %s" % ("\t"* recursion_level, recursion_level, ["IM %s" % ast.get("n")]))
            return ["IM %s" % ast.get("n")]
        elif ast.get("op") == "arg":
            print("%s %s %s" % ("\t" * recursion_level, recursion_level, ["AR %s" % ast.get("n")]))
            print()
            return ["AR %s" % ast.get("n")]
        elif ast.get("a").get("op") in ['imm', 'arg'] and ast.get("b").get("op") in ['imm', 'arg']:
            left = self.pass3(ast.get('a'), recursion_level = recursion_level + 1)
            right = self.pass3(ast.get('b'), recursion_level = recursion_level + 1)
            print("%s %s %s" % ("\t"*recursion_level, recursion_level, left + ['SW'] + right + [self.asm_operations.get(ast.get('op'))]))
            print()
            if self.asm_operations.get(ast.get('op')) in ['SU']:
                return left + ['SW'] + right + ['SW'] + [self.asm_operations.get(ast.get('op'))]
            else:
                return left + ['SW'] + right + [self.asm_operations.get(ast.get('op'))]
        else:
            left = self.pass3(ast.get('a'), recursion_level = recursion_level + 1)
            right = self.pass3(ast.get('b'), recursion_level = recursion_level + 1)
            print("%s %s %s" % ("\t"*recursion_level, recursion_level, left + ["PU"] + right + ["SW", "PO", self.asm_operations.get(ast.get('op'))]))
            print()
            return left + ["PU"] + right + ["SW", "PO",  self.asm_operations.get(ast.get('op'))]     
