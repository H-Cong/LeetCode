# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        
        curr = head
        l = 0
        while curr:
            curr = curr.next
            l += 1
        
        q = k % l 
        
        while q > 0:
            head  = self.rotate(head)
            q -= 1
        
        return head
    
    def rotate(self, head):
        curr = head
        while curr.next.next:
            curr = curr.next
        temp = curr.next
        curr.next = None
        temp.next = head
        
        return temp
    
    # TC: O(n + n*q) = O(n)
    
    # SC: O(q)
