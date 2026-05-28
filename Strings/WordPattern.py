class Solution(object):
    def wordPattern(self, pattern, s):
        palabras = s.split()
        matching = {}
        usadas = set()
        if len(pattern) != len(palabras):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in matching:
                if palabras[i] in usadas:
                    return False
                matching[pattern[i]] = palabras[i]
                usadas.add(palabras[i])
            elif matching[pattern[i]] != palabras[i]:
                return False
        return True
