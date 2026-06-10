class Solution(object):
    def runningSum(self, nums):
        acumulate = 0
        resultado = []
        for i in range(len(nums)):
            acumulate = acumulate + nums[i]
            resultado.append(acumulate)
        return resultado
