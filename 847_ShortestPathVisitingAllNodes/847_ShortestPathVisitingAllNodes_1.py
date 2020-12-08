class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        '''
        BFS + Bitwise Operation
        Similar: 864
        '''
        n = len(graph)
        goal = (1<<n) - 1 # 2
        queue = deque()
        for i in range(n):
            queue.append((0, i, 1<<i))
        visited = set()
        
        while queue:
            length, node, state = queue.popleft()
            if state == goal: return length
            if (node, state) in visited: continue
            visited.add((node, state))
            for next_node in graph[node]:
                queue.append((length+1,next_node, state | (1 << next_node))) # 1
                
        
        return -1
    
    # TC: O(n*2^n)

    # SC: O(n*2^n)
    
    # 1. | is a bitwise or operator. 1000 | 1010 => 1010
    # 2. << is a left shift bitwise operator. 1<<n equals to 2^n except in a binary form.
    #    i.e. 15 = 1111
    
    # ref: https://leetcode.com/problems/shortest-path-visiting-all-nodes/discuss/139748/Python-BFS-with-explaination
