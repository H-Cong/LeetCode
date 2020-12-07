# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        temp = dummy = ListNode(-1)
        r = 0
        while l1 or l2 or r:
            _sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + r
            temp.next = ListNode(_sum % 10)
            temp = temp.next
            r = _sum // 10
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return dummy.next
    
    # TC: O(max(m, n))
    
    # SC: O(max(m, n))
