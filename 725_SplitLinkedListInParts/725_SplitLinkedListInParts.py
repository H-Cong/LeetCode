# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        total_len = 0
        head = root
        # calculate the total length of the linked list
        while head:
            total_len += 1
            head = head.next
            
        ans = []
        
        width = total_len // k
        remainder = total_len % k
        
        prev, head = None, root
        
        for i in range(k):
            ans.append(head)
            # move prev to end of the current subset
            # move head to start of the next subset
            for j in range(width + (1 if remainder > 0 else 0)):
                prev = head
                head = head.next
            # break the link if prev is not the last element of the linked list
            if prev:
                prev.next = None
            
            remainder -= 1
        
        return ans
    
    # TC: O(n+n)
    # n for calculating the length of the linked list
    # n for iterating list to generate the splits
    
    # SC: O(k)
    # k for the k heads in ans, this is the additional space used in writing the answer
