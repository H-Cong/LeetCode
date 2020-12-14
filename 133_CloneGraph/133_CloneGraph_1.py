"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.visited = {}
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        '''
        DFS
        '''
        if not node: return node
        
        if node in self.visited:
            return self.visited[node]
        
        clone_node = Node(node.val, [])
        self.visited[node] = clone_node
        
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]
        
        return clone_node
    
    # TC: O(n + m)
    # where n is a number of nodes and m is a number of edges
    
    # SC: O(n)
    # This space is occupied by the visited hash map and in addition to that, 
    # space would also be occupied by the recursion stack since we are adopting 
    # a recursive approach here. The space occupied by the recursion stack would 
    # be equal to O(h) where h is the height of the graph. Overall, the space complexity would be O(n).
    
    # ref: https://leetcode.com/problems/clone-graph/solution/
        
