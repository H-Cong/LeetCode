# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        '''
        Morris Traversal
        '''
        candidates = []
        prev = TreeNode(float('-inf')) # 9
        while root:
            if root.left:
                temp = root.left
                while temp.right and temp.right != root: # 1
                    temp = temp.right
                if not temp.right:  # 2
                    temp.right = root                     
                    root = root.left  # 3
                else: # 4
                    temp.right = None
                    if prev.val > root.val: # 7
                        candidates += [prev, root]
                    prev = root
                    root = root.right  # 5
            else: # 6
                if prev.val > root.val: # 7
                    candidates += [prev, root]
                prev = root
                root = root.right
        
        candidates[0].val, candidates[-1].val = candidates[-1].val, candidates[0].val # 8
        
                
    # TC: O(n)
    
    # SC: O(1)
    
    # 1. Find the rightmost node "*" on the left subtree of current root.
    #    This "*" node is also the immediate previous node in the InOrder traversal
    # 2. When we find this "*" node, we build a bridge between "*" and root.
    #    This bridge makes root as the child node of "*" node.
    # 3. Then we move root to its left child.
    # 4. This else means temp.right == root, i.e. there is already a bridge between
    #    this rightmost node to the root (or immediate next node for InOrder Traversal).
    #    Then we break this bridge.
    # 5. Then we move root to its right child.
    # 6. This else means there is no left child of current root, i.e. we have reached the 
    #    leftmost node of current node. 
    # 7. In binary search tree, prev val should always be smaller or equal to current val
    #    If prev.val > curr.val, then smh is wrong. We add both nodes to candidate list
    # 8. It doesn`t matter whether the swapped nodes are next to each other or not, 
    #    we only need to swap the first and last value. Just think about it.
    # 9. As previous should always be smaller than current, we init prev to -inf to begin.
    
    # ref: https://stackoverflow.com/questions/5502916/explain-morris-inorder-tree-traversal-without-using-stacks-or-recursion
    # ref: https://docs.google.com/presentation/d/11GWAeUN0ckP7yjHrQkIB0WT9ZUhDBSa-WR0VsPU38fg/edit#slide=id.g61bfb572cf_0_0
    # ref: https://leetcode.com/problems/recover-binary-search-tree/discuss/917430/Python-O(n)O(1)-Morris-traversal-explained
    
    # Tradition Morris Inorder Traversal:
    
    '''
        while root:
            if root.left:
                temp = root.left
                while temp.right and temp.right != root:
                    temp = temp.right
                if not temp.right:
                    temp.right = root                     
                    root = root.left
                else: # 4
                    temp.right = None
                    print(root.val)
                    root = root.right 
            else:
                print(root.val)
                root = root.right
    '''
