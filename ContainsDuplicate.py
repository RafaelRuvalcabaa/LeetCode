def duplicate(nums):
    duplicated = []
    for i in nums: 
        if i in duplicated:
            return True
        duplicated.append(i)
    return False
print(duplicate([1,2,3,4,5,5]))


def setduplicate(nums):
    return len(nums) != set(nums)
print(setduplicate([1,2,3,4,5,5]))