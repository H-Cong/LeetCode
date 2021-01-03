class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        DFS
        '''
        if not grid or not len(grid[0]): return 0
        ans = 0
        seen = set()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    curr = self.dfs(i, j, grid, seen)
                    ans = max(ans, curr)
        
        return ans
    
    def dfs(self, i, j, grid, seen):
        m, n = len(grid), len(grid[0])
        
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0 or (i,j) in seen: return 0
        
        seen.add((i, j))
        
        return (1 + self.dfs(i+1, j, grid, seen) + self.dfs(i-1, j, grid, seen) + self.dfs(i, j+1, grid, seen) + self.dfs(i, j-1, grid, seen))
    
    # TC: O(m*n)
    
    # SC: O(m*n)
    # space comes from both set() and stack recursive usage.
