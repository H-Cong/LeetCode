# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        '''
        Recursion
        '''
        return max(self.helper(root))
    
    def helper(self, node):
        if not node: return [0, 0]
        left = self.helper(node.left)
        right = self.helper(node.right)
        
        # if we rob this node, we cannot rob its children
        rob = node.val + left[1] + right[1]
        
        # else we could choose to either rob its children or not
        not_rob = max(left) + max(right)
        
        return [rob, not_rob]
    
    # TC: O(n) since we visit all nodes once.
    
    # SC: O(n)
    # O(n) since we need stacks to do recursion, and the maximum depth 
    # of the recursion is the height of the tree, which is O(n) in the worst case 
    # and log(n) in the best case.
    
    # ref: https://leetcode.com/problems/house-robber-iii/solution/
