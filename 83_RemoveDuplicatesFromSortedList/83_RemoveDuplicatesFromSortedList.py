# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next # this has to be under else instead of getting excuted in every while loop
        
        return head
    
    # TC: O(N)
    # As each node in the list is checked exactly once
    
    # SC: O(1)
    # No extra space is used
