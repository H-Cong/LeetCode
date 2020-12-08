class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        '''
        BFS + Bitwise Operation
        '''
        row = len(grid)
        col = len(grid[0])
        
        start_r, start_c = -1, -1
        num_k = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "@":
                    start_r, start_c = i, j
                if "a" <= grid[i][j] <= "f":
                    num_k += 1
        
        goal = (1<<num_k) - 1                                      
        queue = deque([(start_r, start_c, 0, 0)]) 
        visited = set()
        
        while queue:
            i, j, state, curr_length = queue.popleft()
            
            if "a" <= grid[i][j] <= "f":
                state |= 1<<(ord(grid[i][j]) - ord("a"))
            
            if state == goal: return curr_length
            if (i, j, state) in visited: continue
            visited.add((i, j, state))
            
            neighbours = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
            
            for x, y in neighbours:
                if 0 <= x < row and 0 <= y < col and self.canVisit(grid[x][y], state):
                    queue.append((x, y, state, curr_length + 1))
        
        return -1
    
    
    def canVisit(self, char, state):
        return char in ".@abcdef" or (char in "ABCDEF" and state & 1<<(ord(char.lower()) - ord("a")) != 0) 
    
    # TC: O(m*n*2^k)
    
    # SC: O(m*n*2^k)
    


