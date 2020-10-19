# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # fast and slow pointers
        slow = head
        fast = head
        
        # NOTE: check both fast and fast.next is not None before the fast.next.next step
        while fast:
            if not fast.next:
                return False
            else:
                fast = fast.next.next
                slow = slow.next
                if fast == slow:
                    return True
        
        return False
    
    # TC: O(N)
    # if no cycle, fast pointer reaches end first and the run time depends on the len(list)
    # if cycle, it will take slow k steps to reach cycle and another constant number p to meet the fast pointer. 
    # Hua Hua Youtube has an equation to prove that fast and slow pointer will always meet if cycle exists.
    
    # SC: O(1) 
    # We only use two nodes (slow and fast) so the space complexity is O(1)
