# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        anterior = None 
        actual = head

        while actual:
            siguiente = actual.next
            actual.next = anterior 
            anterior = actual
            actual = siguiente 

        return anterior 
         
        
# Construyes la lista 1 → 2 → 3
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node1.next = node2
node2.next = node3

# La pasas a tu solución
sol = Solution()
resultado = sol.reverseList(node1)

# La imprimes recorriéndola
actual = resultado
while actual:
    print(actual.val)
    actual = actual.next