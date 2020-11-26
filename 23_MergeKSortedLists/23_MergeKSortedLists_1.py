# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # Brute Force
        # create a temp list to store all values from all linked lists
        temp = []
        # create a dummy listnode and a pointer to iterate it
        dummy = tail = ListNode(0)
        # iterate all linked list and their elements
        for l in lists:
            while l:
                temp.append(l.val)
                l = l.next
        # create a new linked list from the temp list      
        for i in sorted(temp):
            tail.next = ListNode(i)
            tail = tail.next
            
        return dummy.next
    
    # TC: O(N + NlogN + N) = O(NlogN)
    # 1. collecting all the values costs O(N) time
    # 2. a stable sorting algorithm costs O(NlogN) time
    # 3. iteratiing for creating the linked list costs O(N) time
    
    # SC: O(N + N) = O(N)
    # 1. sorting cost O(N) space (depends on the algo you choose)
    # 2. creating a new linked list costs O(N) space
