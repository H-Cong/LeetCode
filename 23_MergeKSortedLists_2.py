# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # Divide And Conquer
        # idea: group two lists together and use the 21 merge two sorted lists approach
        amount = len(lists)
        # check corner case
        if amount == 0:
            return None
        # set interval to 1
        interval = 1
        # group two lists together
        while interval < amount:
            for i in range(0, amount - interval, interval*2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
                
            # increase interval by 2 fold after each for loop
            interval *= 2
        
        return lists[0]
    
    def merge2Lists(self, l1, l2):
        # create dummy head
        dummy = tail = ListNode(0)
        # iterate two lists
        while l1 and l2:
            if l1.val < l2.val:
                # you can use either line below
                tail.next = ListNode(l1.val)
                # tail.next = l1
                l1 = l1.next
            else:
                # you can use either line below
                tail.next = ListNode(l2.val)
                # tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            # Note: it is wrong to use tail = l1.next
            tail.next = l1
        if l2:
            tail.next = l2
            
        return dummy.next
    
    # TC: O(Nlogk), k is the number of linked lists
    # We can merge two sorted linked list in O(n) time where n is the total number of nodes in two lists.
    # Sum up the merge process and we can get: O(Nlogk)
    
    # SC: O(1)
    # The iterative approach only allocates a few pointers, so it has a constant overall memory footprint.
       
    
