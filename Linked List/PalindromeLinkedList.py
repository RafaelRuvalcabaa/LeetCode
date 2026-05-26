class Solution(object):
    def isPalindrome(self, head):
        pali = []
        current = head
        while current is not None: 
            pali.append(current.val)
            current = current.next 
        for i in range(len(pali)):
            if pali[i] != pali[-1-i]:
                return False
        return True
