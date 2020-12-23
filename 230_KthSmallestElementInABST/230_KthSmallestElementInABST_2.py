# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        '''
        Morris Inorder Traversal
        '''
        count = 0
        while root:
            if root.left:
                temp = root.left
                while temp.right and temp.right != root:
                    temp = temp.right
                if not temp.right:
                    temp.right = root
                    root = root.left
                else:
                    count += 1
                    if count == k:
                        return root.val
                    temp.right = None
                    root = root.right
            else:
                count += 1
                if count == k:
                    return root.val
                root = root.right
        
        return None
    
    # TC: O(n)
    # morris traversal is O(n).
    
    # SC: O(1)
    
    
    
        
