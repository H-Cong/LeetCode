# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        '''
        Reverse and Merge
        '''
        if not head: return
        
        fast = slow = head   # 1
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        prev, curr = None, slow # 2
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        
        first, second = head, prev # NOTE the prev here
        
        while second.next: # 3
            first.next, first = second, first.next
            second.next, second = first, second.next
            
    
    # TC: O(n)
    
    # SC: O(1)
    
    # IDEA: first reverse the second half of the linked list
    #       then merge the first half and the reversed second half
    # NOTE: when merging, while should bound by second.next. 
    
    # ref: https://leetcode.com/problems/reorder-list/solution/
