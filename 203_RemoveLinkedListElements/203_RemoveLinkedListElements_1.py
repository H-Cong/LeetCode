# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head: return None
        curr = head
        
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
                continue
            curr = curr.next
        
        if head.val == val: head = head.next # this is to due with when curr.val == val
                                             # instead of curr.next.val == val
        
        return head
    
    # TC: O(n)
    
    # SC: O(1)
