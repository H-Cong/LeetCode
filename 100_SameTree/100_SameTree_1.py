# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        '''
        Recursion
        '''
        return self.helper(p, q)
    
    def helper(self, m, n):
        if not m and not n: return True
        if not m or not n: return False
        if m.val == n.val:
            if self.helper(m.left, n.left) and self.helper(m.right, n.right):
                return True
        else:
            return False
        
    # TC: O(n)
    
    # SC: O(n)
