class Solution(object):
    def preorder(self, root):
        lista = []
        def pre(node):
            if node is None:
                return lista
            lista.append(node.val)
            for child in node.children:
                pre(child)
            return lista
        return pre(root)
