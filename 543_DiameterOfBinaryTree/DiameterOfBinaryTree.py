# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        diameter = [0]
        self.depth(root, diameter)
        return diameter[0]
    
    def depth(self, root, diameter):
        if not root: return 0
        left = self.depth(root.left, diameter)
        right = self.depth(root.right, diameter)
        diameter[0] = max(diameter[0], left + right)
        return 1 + max(left, right)
    
    # TC: O(n)
    
    # SC: O(n)
    
    # if wondering why use a 1 item list, look up value type and reference type
    # ref: https://leetcode.com/problems/diameter-of-binary-tree/discuss/101145/Simple-Python
