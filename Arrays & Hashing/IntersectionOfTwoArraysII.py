class Solution(object):
    def intersect(self, nums1, nums2):
        freq = {}
        for n in nums1:
            freq[n] = freq.get(n, 0) + 1
        res = []
        for n in nums2:
            if freq.get(n, 0) > 0:
                res.append(n)
                freq[n] -= 1
        return res
