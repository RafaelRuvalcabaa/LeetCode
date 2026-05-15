class Solution(object):
    def singleNumber(self, nums):
        visited = []
        for i in range(len(nums)):
            if nums[i] not in visited:
                visited.append(nums[i])
            else:
                visited.remove(nums[i])
        return visited[0]
