# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        '''
        Iteration
        '''
        stack = [(p, q)]
        while stack:
            m, n = stack.pop()
            if not m and not n: continue
            if not m or not n: return False
            if m.val == n.val:
                stack.append((m.left, n.left))
                stack.append((m.right, n.right))
            else: return False
        
        return True
    
    # TC: O(n)
    
    # SC: O(n)
