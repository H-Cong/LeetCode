# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        '''
        DFS
        '''
        if not root: return []
        res = []
        self.dfs(root, '', res)
        return res
    
    def dfs(self, root, curr, res):
        curr += str(root.val)
        if root.left:
            self.dfs(root.left, curr+'->', res) # NOTE: here is + instead of +=
        if root.right:
            self.dfs(root.right, curr+'->', res)
        if not root.left and not root.right:
            res.append(curr)
    
    # TC: O(n)
    
    # SC: O(n)
