class Solution(object):
    def removeElement(self, nums, val):
        left = 0
        right = 0
        while right <= len(nums) - 1:
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
            right += 1
        return left
