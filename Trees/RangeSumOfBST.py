class Solution(object):
    def rangeSumBST(self, root, low, high):
        if root is None:
            return 0
        suma = 0
        if low <= root.val <= high:
            suma += root.val
        suma += self.rangeSumBST(root.left, low, high)
        suma += self.rangeSumBST(root.right, low, high)
        return suma
