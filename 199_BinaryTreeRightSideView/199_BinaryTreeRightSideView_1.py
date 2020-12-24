# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        '''
        DFS: based on 102: Binary Tree Level Order Traversal
        '''
        if not root: return []
        level_traversal = []
        self.dfs(root, 0, level_traversal)
        
        res = []
        for level in level_traversal:
            res.append(level[-1])
        
        return res
    
    def dfs(self, root, level, res):
        if len(res) == level:
            res.append([])
        res[level].append(root.val)
        
        if root.left: self.dfs(root.left, level+1, res)
        if root.right: self.dfs(root.right, level+1, res)
        
        return res
    
    # TC: O(n)
    
    # SC: O(n)
        
