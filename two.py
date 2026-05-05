def two(nums, target): 
    for i in range(len(nums)):
        for j in range(i+1, len(nums)): 
            result = nums[i] + nums[j]
            if result == target:
                return [i, j]

print(two([1,2,3,45,67,8,9,6,4,2,45], 12))
