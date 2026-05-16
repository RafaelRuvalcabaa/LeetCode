class Solution(object):
    def isBalanced(self, root):
        if root is None:
            return True
        izquierdo = self.maxDepth(root.left)
        derecho = self.maxDepth(root.right)
        if abs(izquierdo - derecho) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def maxDepth(self, root):
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
