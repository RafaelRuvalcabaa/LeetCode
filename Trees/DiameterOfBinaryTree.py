class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.maximo = 0
        def depth(root):
            if root is None:
                return 0
            left = depth(root.left)
            right = depth(root.right)
            self.maximo = max(self.maximo, left + right)
            return 1 + max(left, right)
        depth(root)
        return self.maximo
