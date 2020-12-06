# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        '''
        InOrder Traversal
        '''
        value = []
        x = y = float('-inf')
        self.inOrder(root, value)
        # self.findSwappedNumber(value, x, y) # 1
        x, y = self.findSwappedNumber(value, x, y)
        self.recover(root, x, y)
    
    def inOrder(self, root, value):
        if not root: return   # 3
        self.inOrder(root.left, value)
        value.append(root.val)
        self.inOrder(root.right, value)
    
    def findSwappedNumber(self, value, x, y):
        for i in range(len(value) - 1):
            if value[i] > value[i+1]:
                y = value[i+1]
                if x == float('-inf'): x = value[i]  # 2
                else: break
        
        return x, y
                    
    def recover(self, root, x, y):
        if not root: return   # 3
        if root.val == x:
            root.val = y
        elif root.val == y:
            root.val = x
        
        self.recover(root.left, x, y)
        self.recover(root.right, x, y)
        
    # TC: O(n)
    
    # SC: O(n)
    
    # 1. this line wont alter the value of x and y, they will still be -inf
    #    by the time of findSwappedNumber() returns. This differs with c++
    #    ref to this link to see why:
    #    https://stackoverflow.com/questions/575196/
    # 2. This is to deal with when the swapped number are next to each other 
    #    or not.
    # 3. Remember to check corner cases!!!!!
    
    # ref: https://www.youtube.com/watch?v=H3PPKuyzKro
