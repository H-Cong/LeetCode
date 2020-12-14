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
        BFS
        '''
        if not node: return node
        
        visited = {}
        
        queue = deque([node])
        visited[node] = Node(node.val, [])
        
        while queue:
            n = queue.popleft()
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                visited[n].neighbors.append(visited[neighbor])
        
        return visited[node]
    
    # TC: O(n + m)
    # where n is a number of nodes and m is a number of edges
    
    # SC: O(n)
    # This space is occupied by the visited dictionary and in addition to that, 
    # space would also be occupied by the queue since we are adopting the BFS 
    # approach here. The space occupied by the queue would be equal to O(W) where 
    # W is the width of the graph. Overall, the space complexity would be O(N).


    
    # ref: https://leetcode.com/problems/clone-graph/solution/
        
