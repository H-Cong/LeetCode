# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        '''
        Recursion
        '''
        lower, upper = float('-inf'), float('inf')
        return self.helper(root, lower, upper)
    
    def helper(self, root, lower, upper):
        if not root:
            return True
        # if lower < root.val < upper and self.helper(root.right, root.val, upper) and self.helper(root.left, lower, root.val): # this works as well
        if lower < root.val < upper and self.helper(root.left, lower, root.val) and self.helper(root.right, root.val, upper):
            return True
        
        return False
    
    # TC: O(n)
    
    # SC: O(n)
