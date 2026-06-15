class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i != '+' and i != '-' and i != '*' and i != '/':
                stack.append(int(i))
            else:
                a = stack.pop()
                b = stack.pop()
                if i == '+':
                    c = a + b
                elif i == '-':
                    c = b - a
                elif i == '*':
                    c = a * b
                else:
                    c = b / a
                stack.append(int(c))
        return stack.pop()