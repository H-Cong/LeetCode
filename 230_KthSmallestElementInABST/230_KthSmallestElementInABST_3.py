# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        '''
        Recursive
        '''
        l = self.helper(root, [])
        
        return l[k-1]
    
    def helper(self, root, l):
        if root:
            self.helper(root.left, l)
            l.append(root.val)
            self.helper(root.right, l)
        
        return l
    
    # TC: O(n)
    
    # SC: O(n)
    
    
    
        
