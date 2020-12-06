# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        '''
        Iterative with Stack. Similar: 94, 144
        '''
        res, stack = [], []
        
        while root or stack:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.right
            
            root = stack.pop()
            root = root.left
            
        return res[::-1]
    
    # TC: O(n)
    
    # SC: O(n)
