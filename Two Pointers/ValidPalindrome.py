class Solution(object):
    def isPalindrome(self, s):
        limpio = ""
        for i in s:
            if i.isalnum():
                limpio += i.lower()
        izq = 0
        der = len(limpio) -1

        while izq < der:
            if limpio[izq] != limpio[der]:
                return False
            izq += 1
            der -= 1
        return True
    
sol = Solution()

# Caso 1 - debe ser True
print(sol.isPalindrome("A man, a plan, a canal: Panama"))

# Caso 2 - debe ser False
print(sol.isPalindrome("race a car"))

# Caso 3 - debe ser True
print(sol.isPalindrome("racecar"))