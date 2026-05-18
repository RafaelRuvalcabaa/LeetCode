class Solution(object):
    def searchBST(self, root, val):
        if root is None:
            return None
        if val == root.val:
            return root
        if val < root.val:
            return self.searchBST(root.left, val)
        return self.searchBST(root.right, val)
