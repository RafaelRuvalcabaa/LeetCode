class Solution(object):
    def pivotIndex(self, nums):
        sumTotal = sum(nums)
        sumIzq = 0
        for i in range(len(nums)):
            sumDer = sumTotal - sumIzq - nums[i]
            if sumIzq == sumDer:
                return i
            sumIzq += nums[i]
        return -1
