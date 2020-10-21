# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        # As all elements in G are unique, we can turn G from a list to a set
        # Sets in Python are used to store unordered collection of distinct hashable objects
        # Since sets are unordered, you cant access items in a set by referring to an index or a key
        # comparing to list, iterating a set is bit slower than list when iterating over the values, 
        # HOWEVER, sets performs QUITE FASTER when checking the existance of a certain element in it
        # NOTE: it still works if we dont convert list to set, just runs slower
        # in my implementation, it takes 3560ms when using list, but takes 100ms when using set
        
        setG = set(G)
        res = 0
        while head:
            if head.val in setG and (head.next == None or head.next.val not in setG):
                res += 1
            head = head.next
        return res
    
    # TC: O(N + G.length) where N is the length of the linked list with root node head
    # SC: O(G.length) to store setG
