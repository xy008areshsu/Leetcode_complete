"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""

class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        st = []

        for t in tokens:
            if t not in '+-*/':
                st.append(float(t))
            else:
                if len(st) < 2:
                    raise Exception('Not enough operants')
                op2 = st.pop()
                op1 = st.pop()
                if t == '+':
                    res = op1 + op2
                elif t == '-':
                    res = op1 - op2
                elif t == '*':
                    res = op1 * op2
                else:
                    res = op1/op2
                st.append(res)

        if len(st) < 1:
            raise Exception('Wrong!')

        return st.pop()

