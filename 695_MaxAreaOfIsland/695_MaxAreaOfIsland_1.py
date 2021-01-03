class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        DFS
        '''
        if not grid or not len(grid[0]): return 0
        ans = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    curr = self.dfs(i, j, grid)
                    ans = max(ans, curr)
        
        return ans
    
    def dfs(self, i, j, grid):
        m, n = len(grid), len(grid[0])
        
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0: return 0
        
        grid[i][j] = 0
        
        return (1 + self.dfs(i+1, j, grid) + self.dfs(i-1, j, grid) + self.dfs(i, j+1, grid) + self.dfs(i, j-1, grid))
    
    # TC: O(m*n)
    
    # SC: O(m*n)
    # though in-place mutation is employed. The SC is still mn as the recursive call takes stack memory.
