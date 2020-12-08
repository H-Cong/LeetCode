class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        '''
        BFS
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
        
        keys = tuple([False]*num_k)                                          # 1
        queue = deque([(start_r, start_c, keys, 0)]) # 0 is the path length
        visited = set((start_r, start_c, keys))
        
        while queue:
            i, j, curr_keys, curr_length = queue.popleft()
            
            if "a" <= grid[i][j] <= "f" and not curr_keys[ord(grid[i][j]) - ord("a")]:
                curr_keys = self.addKeys(curr_keys, grid[i][j])
                if all(curr_keys): return curr_length                        # 2
            
            neighbours = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
            
            for x, y in neighbours:
                if 0 <= x < row and 0 <= y < col and (x, y, curr_keys) not in visited and self.canVisit(grid[x][y], curr_keys):
                    visited.add((x, y, curr_keys))
                    queue.append((x, y, curr_keys, curr_length + 1))
        
        return -1
    
    def addKeys(self, keys, char):
        keys = list(keys)
        keys[ord(char) - ord("a")] = True
        
        return tuple(keys)
    
    def canVisit(self, char, keys):
        return char in ".@abcdef" or (char in "ABCDEF" and keys[ord(char.lower()) - ord("a")])  # 3
    
    # TC: O(row*col*K!) where K is the number of keys
    # This is O(mnk!) not (Omn2^k) because your keys depend on in which order 
    # keys are discovered. So the number of states is permutations of keys, 
    # which is k!. To make it 2^k, you should assign unique orders for each 
    # key (e.g. by sorting or using bits).
    
    # SC: O(row*col*K)
    # I think. Not sure. Space should mainly come from the visited set.
    
    # 1. keys is set to tuple because when check (x, y, curr_keys) in visited, 
    #    we need this curr_keys to be hashable. An error will be raised if we 
    #    set keys to a list
    # 2. all() checks whether every element in curr_keys is Ture
    # 3. we need to include "@" because the start point can be visited multiple times
    
    # ref: https://leetcode.com/problems/shortest-path-to-get-all-keys/discuss/406120/

