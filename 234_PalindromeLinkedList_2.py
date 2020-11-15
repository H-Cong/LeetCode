# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head: return True
        
        first_half_end = self.end_of_first_half(head)
        reversed_second_half = self.reverse(first_half_end.next)
        
        first_half = head
        second_half = reversed_second_half
        
        """
        if we dont put both halfs in this while statement, we may get a "NoneType has no .val" error 
        as first half may be one node longer than second half
        """
        while first_half and second_half: 
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next
        
        restored_second_half = self.reverse(reversed_second_half)
        
        return True
        
    
    def end_of_first_half(self, head):
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        return slow
    
    def reverse(self, head):
        _reversed = None
        curr = head
        while curr:
            temp_node = curr.next
            curr.next = _reversed
            _reversed = curr
            curr = temp_node
        
        return _reversed
    
    # TC: O(n) where n is the number of nodes in the Linked List
    # Finding the middle is O(n), reversing a list in place is O(n), 
    # and then comparing the 2 resulting Linked Lists is also O(n)

    # SC: O(1)
    # We are changing the next pointers for half of the nodes. This was all memory that had 
    # already been allocated, so we are not using any extra memory and therefore it is O(1).
    
    """
    some people on the discussion forum saying it has to be O(n) because we're creating a new list. 
    This is incorrect, because we are changing each of the pointers one-by-one, in-place. We are not 
    needing to allocate more than O(1) extra memory to do this work, and there is O(1) stack frames 
    going on the stack. It is the same as reversing the values in an Array in place (using the 
    two-pointer technique).
    """
