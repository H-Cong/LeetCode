# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        '''
        Recursion
        '''
        if not root: return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
    
    # TC: O(n)
    # Since each node in the tree is visited only once, the time complexity is O(n), 
    # where nn is the number of nodes in the tree. We cannot do better than that, 
    # since at the very least we have to visit each node to invert it.
    
    # SC: O(n)
    # Because of recursion, O(h) function calls will be placed on the stack in the 
    # worst case, where hh is the height of the tree. Because h ∈ O(n), 
    # the space complexity is O(n).
    
    # IDEA: essentially, we are just inverse first parents nodes, then inverse the child
    # node of each parent.
