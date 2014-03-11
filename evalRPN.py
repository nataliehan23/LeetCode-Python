# Evaluate the value of an arithmetic expression in Reverse Polish Notation.

# Valid operators are +, -, *, /. Each operand may be an integer or another expression.

# Some examples:
#   ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#   ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        op = set(['+','-','*','/'])
        for t in tokens:
            if t not in op:
                
                stack.append(int(t))
            else:
                n2 = stack.pop()
                n1 = stack.pop()
                if t == '+':
                    stack.append(n2+n1)
                elif t == '-':
                    stack.append(n1-n2)
                elif t == '*':
                    stack.append(n1*n2)
                elif t == '/':
                    tmp = float(n1)/float(n2)
                    stack.append(int(tmp))
        res = stack.pop()
        return res
        