# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        '''
        Recursion. DFS.
        '''
        if not root: return []
        res = []
        self.helper(root, 0, res)
        
        return res
    
    def helper(self, root, level, res):
        if len(res) == level:
            res.append(deque())
            
        if level % 2 == 0:
            res[level].append(root.val)
        else:
            res[level].appendleft(root.val)

        if root.left: self.helper(root.left, level + 1, res)
        if root.right: self.helper(root.right, level + 1, res)
            
    # TC: O(n)
    
    # SC: O(n)
    
    # appendleft() is a O(1) function
