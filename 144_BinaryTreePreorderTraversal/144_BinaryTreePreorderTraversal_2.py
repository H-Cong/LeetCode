# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        '''
        Iterative with Stack.
        '''
        res, stack = [], []
        
        while root or stack:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            root = root.right
        
        return res
    
    # TC: O(n)
    
    # SC: O(n)
