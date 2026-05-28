class Solution(object):
    def findTheDifference(self, s, t):
        contador = {}
        for i in range(len(s)):
            letra = s[i]
            if letra in contador:
                contador[letra] += 1
            else:
                contador[letra] = 1
        for j in range(len(t)):
            if t[j] in contador:
                contador[t[j]] -= 1
                if contador[t[j]] == -1:
                    return t[j]
            else:
                return t[j]
