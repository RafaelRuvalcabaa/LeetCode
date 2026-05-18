class Solution(object):
    def hasPathSum(self, root, targetSum):
        if root is None:
            return False
        if root.left is None and root.right is None:
            return root.val == targetSum
        if self.hasPathSum(root.left, targetSum - root.val):
            return True
        if self.hasPathSum(root.right, targetSum - root.val):
            return True
        return False
