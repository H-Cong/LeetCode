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
        
        inorder_map = {val: i for i, val in enumerate(inorder)}
        preorder = deque(preorder)
        return self.dfs_helper(inorder_map, preorder, 0, len(inorder) - 1)
    
    
    def dfs_helper(self, inorder_map, preorder, left, right):
        if left > right: return None
        node = preorder.popleft()
        root = TreeNode(node)
        root_index = inorder_map[node]
        root.left = self.dfs_helper(inorder_map, preorder, left, root_index - 1)
        root.right = self.dfs_helper(inorder_map, preorder, root_index + 1, right)
        return root
        
    # TC: O(n)

    # SC: O(n)

    # same idea. But all functions in dfs_helper() is O(1) now.
    # deque() to make the pop() O(1) as well
