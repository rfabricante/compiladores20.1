import tatsu
from random import randrange

class ListCompSemantics(object):
    def tt(self, ast):
        return True

    def ff(self, ast):
        return False
    
    def number(self, ast):
        return int(ast)

    def addition(self, ast):
        return ast.left + ast.right

    def subtraction(self, ast):
        return ast.left - ast.right

    def multiplication(self, ast):
        return ast.left * ast.right

    def division(self, ast):
        return ast.left / ast.right

    def id(self, ast):
        return ast

    def conjunction(self, ast):
        return lambda _ : ast.left(_) and ast.right(_)
    
    def disjunction(self, ast):
        return lambda _ : ast.left(_) or ast.right(_)

    def negation(self, ast):
        return lambda _ : not ast.be(_)

    def gt_left_id(self, ast):
        def f(x):
            if type(ast.right) == int:
                r = ast.right
            else:
                r = ast.right(x)
            return x > r
        return f
        
    def gt_right_id(self, ast):
        # Do your magic here !
        def f(x):
            if type(ast.left) == int:
                l = ast.left
            else:
                l = ast.left(x) 
            return l > x 
        return f        
        
    def gt_all_exp(self, ast):
        # Do your magic here !
        return lambda x : ast.left(x) > ast.right(x)
        
    def equal_left_id_exp(self, ast):
        # Do your magic here !
        def f(x):
            if type(ast.right) == int:
                r = ast.right
            else:
                r = ast.right(x)
            return x == r
        return f
        
    def equal_right_id_exp(self, ast):
        # Do your magic here !
        def f(x):
            if type(ast.left) == int:
                l = ast.left
            else:
                l = ast.left(x) 
            return x == l
        return f    
    
    def equal_all_exp(self, ast):
        # Do your magic here !
        return lambda x : ast.left(x) == ast.right(x)
        
    def list_exp(self, ast):
        if type(ast.l) == int:
            print(ast.e)
            return list(filter(lambda _ : ast.e(_), [ast.l]))
        else:
            print(ast.e)   
            assert(type(ast.l) == list)
            return list(filter(lambda _ : ast.e(_), ast.l))
        
def interp():
    grammar = open('list_comp.ebnf').read()
    parser = tatsu.compile(grammar)

    nl = []
    for i in range(100):
        nl.append(randrange(100))
    l =  '[x in {num_list} | (x == 10) or (x > 2)]'.format(num_list = nl)
    ast = parser.parse(l, semantics=ListCompSemantics())
    print(ast)

def main():
    interp()

if __name__ == '__main__':
    main()
