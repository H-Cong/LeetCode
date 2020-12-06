# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        '''
        Morris Traversal. Similar: 94
        '''
        res = []
        
        while root:
            if root.left:
                temp = root.left
                while temp.right and temp.right != root:
                    temp = temp.right
                if not temp.right:
                    res.append(root.val) # only one line change vs Inorder traversal
                    temp.right = root
                    root = root.left
                else:
                    temp.right = None  # Inorder will append root.val here
                    root = root.right
            else:
                res.append(root.val)
                root = root.right
                
        return res
    
    # TC: O(n)
    
    # SC: O(1)
