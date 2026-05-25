class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        contador = {}
        for c in magazine:
            if c not in contador:
                contador[c] = 1
            else:
                contador[c] += 1

        for i in range(len(ransomNote)):
            if ransomNote[i] not in contador:
                return False
            contador[ransomNote[i]] -= 1
            if contador[ransomNote[i]] < 0:
                return False
        return True
