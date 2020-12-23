# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        '''
        Morris Traversal + MinHeap. MinHeap is a overkill here later I found. See solution 2.py
        '''
        ans = []
        heapq.heapify(ans)
        while root:
            if root.left:
                temp = root.left
                while temp.right and temp.right != root:
                    temp = temp.right
                if not temp.right:
                    temp.right = root
                    root = root.left
                else:
                    if not ans or len(ans) < k:
                        heapq.heappush(ans, root.val)
                    else:
                        if ans[-1] > root.val:
                            heapq.heappop(ans, ans[-1])
                            heapq.heappush(ans, root.val)
                    temp.right = None
                    root = root.right
            else:
                if not ans or len(ans) < k:
                        heapq.heappush(ans, root.val)
                        print(3, ans)
                else:
                    if ans[-1] > root.val:
                        heapq.heappop(ans, ans[-1])
                        heapq.heappush(ans, root.val)
                root = root.right
        
        return ans[-1]
    
    # TC: O(nlogk)
    # morris traversal is O(n), heappush/pop is O(logk)
    
    # SC: O(k)
    # space taken by min heap
    
    
        
