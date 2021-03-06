# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        '''
        Morris traversal. Similar: 94, 144
        '''
        res = deque()
        
        while root:
            if root.right:
                temp = root.right
                while temp.left and temp.left != root:
                    temp = temp.left
                if not temp.left:
                    res.appendleft(root.val)
                    temp.left = root
                    root = root.right
                else:
                    temp.left = None
                    root = root.left
            else:
                res.appendleft(root.val)
                root = root.left
                
        return res
    
    # TC: O(n)
    
    # SC: O(1)
    # It is very similar to the pre-order one, except that now we are doing everything reversely.
    # By this I mean we go along the direction of right child and link the leftmost child on the
    # right sub tree to the root. Then we leftappend the val to the result.

    # ref: https://leetcode.com/problems/binary-tree-postorder-traversal/discuss/961894/
