# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        '''
        Iteration
        '''
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            root, lower, upper = stack.pop()
            if not root: continue
            if lower < root.val < upper:
                stack.append((root.left, lower, root.val))
                stack.append((root.right, root.val, upper))
            else:
                return False
        
        return True
        
    # TC: O(n)
    
    # SC: O(n)
