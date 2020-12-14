# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        '''
        DFS Recursion
        '''
        if not root: return None
        self.res = float('-inf')
        self.helper(root)
        return self.res
    
    def helper(self, node):
        if not node: return 0   # 1
        
        left_gain = max(self.helper(node.left), 0)  # 2
        right_gain = max(self.helper(node.right), 0)
        
        curr_path_max = node.val + left_gain + right_gain # 3
        self.res = max(self.res, curr_path_max) 
        
        return node.val + max(left_gain, right_gain)  # 4
    
    # TC: O(n)
    # where n is number of nodes, since we visit each node not more than 2 times.
    
    # SC: O(h)
    # where h is a tree height, to keep the recursion stack. 
    # In the average case of balanced tree, the tree height h = log(n), 
    # in the worst case of skewed tree, h = n.
    
    # NOTE:
    # 1. if a child does not exist, then the value of that child set to 0. 
    #    meaning that we can abandon that child essentially.
    # 2. we check the gain from the left subtree/child of CURRENT NODE.
    #    same for the right_gain.
    # 3. curr_path_max means use the CURRENT NODE as the connection point for the 
    #    left subtree and right subtree.
    # 4. when return to the parent node, we can only return one subtree of CURRENT 
    #    node, since the parent node in the upper level will serve as the connection point
    
    # ref: https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/603423/
