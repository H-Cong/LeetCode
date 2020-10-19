# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l2.next, l1)
            return l2
    
        # TC: O(m+n) m+n is the worst case O(min(m,n)) is the best case
        # TC: O(N)
        
        # SC: O(m+n)
        # The first call to mergeTwoLists does not return until the ends of both l1 and l2 have been reached, 
        # so n + mn+m stack frames consume O(n + m)O(n+m) space.
