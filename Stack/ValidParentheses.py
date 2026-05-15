class Solution(object):
    def isValid(self, s):
        stack = []
        pares = {')': '(', ']': '[', '}': '{'}

        for i in s:
            if i in "([{":
                stack.append(i)
            elif i in ")]}":
                if stack == []:
                    return False
                ultimo = stack.pop()
                if ultimo != pares[i]:
                    return False

        if stack == []:
            return True
        else:
            return False
