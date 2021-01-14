# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        '''
        Two pointers
        '''
        before = before_h = ListNode(0)
        after = after_h = ListNode(0)
        
        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            
            head = head.next
            
        after.next = None
        before.next = after_h.next
        
        return before_h.next
    
    # TC: O(n)
    
    # SC: O(1)
    # Because it only reassigns node reference and doesn't create new nodes.
    
    # ref: https://leetcode.com/problems/partition-list/solution/
