# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1, n2 = l1, l2
        m1, m2 = 0, 0
        while n1:
            m1 = m1*10 + n1.val
            n1 = n1.next
        while n2:
            m2 = m2*10 + n2.val
            n2 = n2.next
        
        ans = m1+m2
        ans = str(ans)
        temp = res = ListNode(-1)
        for c in ans:
            temp.next = ListNode(int(c))
            temp = temp.next
        # temp = None
        return res.next
    
    # TC: O(n1 + n2)
    
    # SC: O(max(n1, n2))
            
            
