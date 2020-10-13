#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        h = ListNode(0)
        p, carry = h, 0
        while l1 or l2:
            Sum = carry
            if l1:
                Sum, l1 = Sum + l1.val, l1.next
            if l2:
                Sum, l2 = Sum + l2.val, l2.next
            p.next, carry = ListNode(int(Sum % 10)), int(Sum / 10)
            p = p.next
        p.next = ListNode(carry) if carry else None
        return h.next

l1 = ListNode(2)
l1.next = ListNode(1)
l1.next.next = ListNode(9)

l2 = ListNode(1)
l2.next = ListNode(5)
l2.next.next = ListNode(8)

sol = Solution()
l3 = sol.addTwoNumbers(l1, l2)

while l3 != None:
    print(l3.val)
    l3 = l3.next

