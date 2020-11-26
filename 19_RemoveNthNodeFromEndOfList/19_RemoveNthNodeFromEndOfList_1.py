# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        '''
        Two Pass solution
        '''
        prev = dummy = ListNode(0)
        prev.next = curr = head
        l = 0
        while curr:
            l += 1
            curr = curr.next
            
        curr = head
        count = 1
        while curr:
            if count != l - n + 1:
                prev = curr
                curr = curr.next
                count += 1
            else:
                prev.next = curr.next
                return dummy.next
        
        return None
    
    # TC: O(n) where n is the length of the ListNode
    
    # SC: O(1)
