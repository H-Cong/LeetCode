"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        VisitedDict = {}
        curr = head
        while curr:
            VisitedDict[curr] = Node(curr.val, None, None)
            curr = curr.next
        
        curr = head
        while curr:
            # VisitedDict[curr].next = VisitedDict[curr.next]
            # VisitedDict[curr].random = VisitedDict[curr.random]
            VisitedDict.get(curr).next = VisitedDict.get(curr.next)
            VisitedDict.get(curr).random = VisitedDict.get(curr.random)
            curr = curr.next
            
        # return VisitedDict[head]
        return VisitedDict.get(head)
    
    # TC: O(2*n)
    # two while loops
    
    # SC: O(n)
    # dict takes O(n) space
    
    """
    NOTE:
    1. Here we need to use dict.get(key) instead of dict[key] to return the value of the key
       This is due to curr.next or curr.random or even head can be None. 
       If we use dict[None], we will get a keyerror wherease dict.get(key) provides a default
       value if the key is missing in dict. If no default value is provided by programmer, None
       will be used as the default value.
    2. In the second while loop, it is wrong to use VisitedDict.get(curr).next = curr.next 
       as this will link the new linked list node to the old linked list node.
    """
