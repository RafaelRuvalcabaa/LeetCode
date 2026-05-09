class Solution(object):
    def maxSubArray(self, nums):
        suma_actual = nums[0]
        resultado = nums[0]
        for i in nums[1:]:
           suma_actual = max(i, suma_actual + i)
           resultado = max(resultado, suma_actual)
        return resultado
        