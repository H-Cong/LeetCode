# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        curr = head
        l = 0
        seen = {}
        
        while curr:
            l += 1
            seen[l] = curr
            curr = curr.next
        
        if l == n:
            return head.next
        
        seen[l - n].next = seen[l - n + 1].next
        
        return head

    
    # TC: O(n) where n is the length of the ListNode
    
    # SC: O(n)
