# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        '''
        Iterative
        '''
        dummy = ListNode(0)
        dummy.next = head
        curr, prev = head, dummy
        for _ in range(m-1):
            curr, prev = curr.next, prev.next
        
        for _ in range(n-m):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
               
        return dummy.next
    
    
    # TC: O(n)
    
    # SC: O(1)
    
    # IDEA: The idea is simple and intuitive: find linkedlist [m, n], 
    # reverse it, then connect m with n+1, connect n with m-1
    
    # ref: https://leetcode.com/problems/reverse-linked-list-ii/discuss/30672/Python-one-pass-iterative-solution
    
    
