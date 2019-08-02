# An infix expression based approach 
# Idea: Construct a tree to store the arithematic expression and evaluvate based on recursive infix eval 

# Use inheritance and concepts of interfaces and polymorphism to get value of a node. 


class Expression:
    def __init__(self,obj):
        self.obj = obj
        
    def get_val(self):
        pass
    
class Operand(Expression):        
    def get_val(self):
        return self.obj
    
class Operator(Expression):
     def get_val(self):
        return self.obj
        
class ExpressionTree(Expression):
    def __init__(self, obj):
        print(obj)
        self.opr  = obj['opr']
        self.op1  = obj['op1']
        self.op2  =  obj['op2']
        
    def get_val(self):
        val1 = self.op1.get_val()
        val2 = self.op2.get_val()
        operator = self.opr.get_val()
        
        # use dictionary for more options
        if operator == '*':
            return val1 * val2 
        elif operator == '+':
            return val1 + val2 
    
op1 = Operand(1)
op2 = Operand(2)
plus= Operator('+')

sub_exp_tree  =  ExpressionTree({'op1' : op1, 'op2' : op2, 'opr' :plus })
tree1 = ExpressionTree({'op1' : sub_exp_tree, 'op2' : op2, 'opr' :plus })
print(tree1.get_val())
