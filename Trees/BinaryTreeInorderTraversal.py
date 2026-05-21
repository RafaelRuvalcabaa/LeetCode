# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        result = []
        def inorder(nodo): 
            if nodo is None:
                return 
            inorder(nodo.left)
            result.append(nodo.val)
            inorder(nodo.right)
        inorder(root)
        return result
