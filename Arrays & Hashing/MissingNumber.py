class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        operador = n * (n + 1) // 2
        result = operador - sum(nums)
        return result
