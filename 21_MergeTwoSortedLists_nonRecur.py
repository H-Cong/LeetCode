# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # create a dummy head with value of -1
        res = ListNode(-1)
        temp_head = res
        
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                temp_head.next = l1
                l1 = l1.next
            else:
                temp_head.next = l2
                l2 = l2.next
            temp_head = temp_head.next
        
        if l1:
            temp_head.next = l1
        if l2:
            temp_head.next = l2
        
        # by returning .next we left out the dummy head which has the value of -1
        return res.next
    
        # TC: O(m+n) m+n is the worst case O(min(m,n)) is the best case
        # TC: O(N)
        
        # SC: O(1)
        # The iterative approach only allocates a few pointers, so it has a constant overall memory footprint.
