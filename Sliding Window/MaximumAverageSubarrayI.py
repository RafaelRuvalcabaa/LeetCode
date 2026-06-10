class Solution(object):
    def findMaxAverage(self, nums, k):
        maxAverage = []
        for i in range(len(nums)- k + 1):
            final = []
            right = i + k -1 
            while i <= right:
                final.append(nums[right])
                right -=1
            average = sum(final)/len(final)
            maxAverage.append(average)
        return max(maxAverage)
