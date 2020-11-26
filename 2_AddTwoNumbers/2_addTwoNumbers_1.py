# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # dummy head can have any value like 0, -1, ... it doesn`t matter
        dummy = ListNode(0)
        # A temp pointer that will always move rightwards in while loop
        temp_pointer = dummy
        
        _sum = 0
        
        # 0 in while loop is taken as False
        while l1 or l2 or _sum:
            _sum += (l1.val if l1 else 0) + (l2.val if l2 else 0) # calculate sum
            temp_pointer.next = ListNode(_sum % 10) # temp.next is actually the same as current l1/l2 position
            temp_pointer = temp_pointer.next
            _sum //= 10 # check whether a carry number exists w.r.t. _sum is larger or smaller than 10
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
        return dummy.next
    
    # TC: O(max(m, n))
    # the algorithm above iterates at most max(m,n) times
    
    # SC: O(max(m, n))
    # The length of the new list is at most max(m,n)+1.
