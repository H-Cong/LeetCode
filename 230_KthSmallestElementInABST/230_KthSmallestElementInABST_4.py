# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        '''
        Iterative
        '''
        l, stack = [], []
        
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            l.append(root.val)
            root = root.right
        
        return l[k-1]
    
    # TC: O(n)
    
    # SC: O(n)
    
    
    
        
