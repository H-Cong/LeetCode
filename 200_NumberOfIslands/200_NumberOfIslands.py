class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        row = len(grid)
        col = len(grid[0])
        ans = 0
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    ans += 1
                    self._dfs(grid, i, j, row, col)
        
        return ans
    
    def _dfs(self, grid, i, j, row, col):
        if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        self._dfs(grid, i+1, j, row, col)
        self._dfs(grid, i-1, j, row, col)
        self._dfs(grid, i, j+1, row, col)
        self._dfs(grid, i, j-1, row, col)
        
        
    # TC: O(m*n)
    # As we just traverse this matrix at most twice? e.g. matrix filled up with 1s
    # First we turn all 1s to 0s, then we scan all 0s
    
    # SC: O(m*n)
    # worst case O(M*N) in case that the grid map is filled with lands where DFS goes by m*n deep.
    # every recursive call will cost 1 stack memory to store like return address etc.
