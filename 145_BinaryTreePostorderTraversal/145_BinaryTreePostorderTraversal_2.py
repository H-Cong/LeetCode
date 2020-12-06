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
        res, stack = deque(), []
        
        while root or stack:
            while root:
                stack.append(root)
                res.appendleft(root.val)
                root = root.right
            
            root = stack.pop()
            root = root.left
            
        return res
    
    # TC: O(n)
    
    # SC: O(n)
