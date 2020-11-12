# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        ans = None
        curr = head
        
        while curr:
            temp = curr.next
            curr.next = ans
            ans = curr
            curr = temp
            
            # curr.next, ans, curr = ans, curr, curr.next # you can use this Python swap to avoid 
                                                          # the use of temp variable
            
        return ans
    
    # TC: O(n)
    # n is the list`s length
    
    # SC: O(1)
    # we are just re-wiring node to another linked list, by the time it finishes, head will be an empty linkedlist
    # so no extra space used here
