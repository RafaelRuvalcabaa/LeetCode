class Solution(object):
    def dfs(self, root, hojas):
        if root is None:
            return
        if root.left is None and root.right is None:
            hojas.append(root.val)
        if root.left:
            self.dfs(root.left, hojas)
        if root.right:
            self.dfs(root.right, hojas)

    def leafSimilar(self, root1, root2):
        hojas1 = []
        hojas2 = []
        self.dfs(root1, hojas1)
        self.dfs(root2, hojas2)
        return hojas1 == hojas2
