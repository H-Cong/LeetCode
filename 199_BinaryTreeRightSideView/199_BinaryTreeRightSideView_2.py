# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        '''
        DFS: Improved.
        '''
        if not root: return []
        res = []
        self.dfs(root, 0, res)
        
        return res
    
    def dfs(self, root, level, res):
        if len(res) == level:
            res.append(root.val)
        else:
            res[level] = root.val
        
        if root.left: self.dfs(root.left, level+1, res)
        if root.right: self.dfs(root.right, level+1, res)
        
        return res
    
    # TC: O(n)
    
    # SC: O(n)

    # IDEA: the last change of each level is the right most number.
