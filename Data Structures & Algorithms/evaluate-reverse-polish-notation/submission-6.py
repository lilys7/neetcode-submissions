class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #every time on the stack, until we reach an operator we push to the stack. then we pop off the top two elts and perform the operation. push the result back to the stack. repeat until list is done.
        stack = []
        operators = {'+', '-', '*', '/'}
        res = 0
        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                s = stack.pop() #2 3
                f = stack.pop() #1 3
                if t == '+':
                    res = f + s #res = 3
                elif t == '-':
                    res = f - s
                elif t == '*':
                    res = f * s
                else:
                    res = int(f / s)
                stack.append(int(res))
        return stack[0]
