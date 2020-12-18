# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        '''
        Recursion
        '''
        if not inorder: return None
        root = TreeNode(preorder.pop(0))
        inorderIndex = inorder.index(root.val)
        root.left = self.buildTree(preorder, inorder[:inorderIndex])
        root.right = self.buildTree(preorder, inorder[inorderIndex+1:])

        return root

    # TC: O(n^2)

    # SC: O(n) I think if counting the recursive stack memory

    # IDEA:
    # use preorder to find the root
    # find the index of root in inorder using root.val
    # split inorder with the root_index
    # recursive call to left and right subtree of the root

    # ref: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34613/A-Python-recursive-solution
    # ref: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34579/Python-short-recursive-solution.
