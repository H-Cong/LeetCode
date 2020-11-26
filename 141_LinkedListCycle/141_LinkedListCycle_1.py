# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # hash table
        # In Python, dict is a hash mapping or hash table
        visited = {}
        while head:
            if head in visited:
                return True
            else:
                visited[head] = 1
                head = head.next
        
        return False
    
    # TC: O(N)
    # each of the n elements in the list will be visited at most once
    # add a node to hash table or check whether a key exists in hash table are
    # both O(1) time
    
    # SC: O(N) 
    # this is for the space taken by the hash table
