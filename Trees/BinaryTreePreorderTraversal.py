# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        result = []
        def preorder(nodo): 
            if nodo is None:
                return 
            result.append(nodo.val)
            preorder(nodo.left)
            preorder(nodo.right)
        preorder(root)
        return result
