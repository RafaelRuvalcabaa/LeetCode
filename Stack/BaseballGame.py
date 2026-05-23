class Solution(object):
    def calPoints(self, operations):
        stack = []
        for op in operations:
            try:
                num = int(op)
                stack.append(num)
            except ValueError:
                if op == "+":
                    ultimo = stack[-1]
                    penultimo = stack[-2]
                    stack.append(ultimo + penultimo)
                elif op == "D":
                    stack.append(stack[-1] * 2)
                elif op == "C":
                    stack.pop()
        return sum(stack)
