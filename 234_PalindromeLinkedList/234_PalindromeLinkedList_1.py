# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        temp = []
        curr = head
        while curr:
            temp.append(curr.val)
            curr = curr.next
            
        i, j = 0, len(temp)-1
        while i < j:
            if temp[i] != temp[j]:
                return False
            i += 1
            j -= 1
        
        return True
    
    # TC: O(n)
    
    # SC: O(n)
