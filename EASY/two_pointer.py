class Water(object):
    def __main__(self, arr): 
        self.arr = arr 

    def counter(arr): 
        left = 0 
        right = len(arr)-1 
        altura = 0
        result = 0
        while left < right:
            agua = min(height[left], height[right]) * (right - left)
            result = max(result, agua)
            if altura[left] < altura[right]:
                left += 1

            else:
                right -= 1 
