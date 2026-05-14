class Solution(object):
    def sortedSquares(self, nums):
        left = 0 
        right = len(nums) -1
        pos = len(nums)-1
        result = [0] * len(nums)
        while left <= right: 
            if abs(nums[left])>abs(nums[right]):
                result[pos] = nums[left] * nums[left]
                pos -=1
                left +=1
            else: 
                result[pos] = nums[right] * nums[right]
                pos -=1
                right -=1
        return result