# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # Merge Sort Top-down
        
        # check corner case
        if not head or not head.next:
            return head
        
        # define slow and fast pointers
        slow = head
        fast = head.next
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # mid is the head of the second half of the splited list
        mid = slow.next
        # break the first half from the second half of the list
        slow.next = None
        
        return self.merge(self.sortList(head), self.sortList(mid))
    
    def merge(self, l1, l2):
        # create dummy head
        dummy = tail = ListNode(0)
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
            
        return dummy.next
    
    # TC: O(NlogN) where n is the number of nodes in linked list. 
    # split: The recursion tree expands in form of a complete binary tree, splitting the list into two halves recursively. The number of levels in a complete binary tree is given by log_2(n)
    # merge: At each level, we merge n nodes which takes O(n) time.
    
    # SC: O(logN) where n is the number of nodes in linked list
    # Since the problem is recursive, we need additional space to store the recursive call stack. The maximum depth of the recursion tree is logn
