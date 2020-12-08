class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        '''
        BFS Similar: 864
        This is slower than bitwise operation
        '''
        n = len(graph)
        
        visited = set()
        states = tuple([False]*n)
        queue = deque()
        for i in range(n):
            queue.append((0, i, states))
        
        while queue:
            length, node, state = queue.popleft()
            state = self.addState(node, state)
            if all(state): return length
            if (node, state) in visited: continue
            visited.add((node, state))
            for next_node in graph[node]:
                queue.append((length+1,next_node, state)) # 1
                
        return -1
    
    def addState(self, node, state):
        state = list(state)
        state[node] = True
        return tuple(state)
    
    # TC: O(n*2^n)

    # SC: O(n*2^n)
    
