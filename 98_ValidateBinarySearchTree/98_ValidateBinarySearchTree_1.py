# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        '''
        Morris InOrder Traversal
        '''
        prev = TreeNode(float('-inf'))
        while root:
            if root.left:
                temp = root.left
                while temp.right and temp.right != root:
                    temp = temp.right
                if not temp.right:
                    temp.right = root
                    root = root.left
                else:
                    if prev.val >= root.val:
                        return False
                    temp.right = None
                    prev = root
                    root = root.right
            else:
                if prev.val >= root.val:
                    return False
                prev = root
                root = root.right
            
        return True
    
    # TC: O(n)
    
    # SC: O(1)
