class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        '''
        DFS
        '''
        if not matrix or not matrix[0]: return 0
        
        row = len(matrix)
        col = len(matrix[0])
        cache = [[0]*col for _ in range(row)]
        ans = 0
        
        for i in range(row):
            for j in range(col):
                # if cache[i][j] == 0:
                ans = max(ans, self.dfs(matrix, i, j, cache))
        
        # return max(max(cache))      # 1
        return ans
    
    def dfs(self, matrix, i, j, cache):
        if cache[i][j] != 0: return cache[i][j]
        
        row = len(matrix)
        col = len(matrix[0])
        curr = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for d in directions:
            x, y = i + d[0], j + d[1]
            if 0 <= x < row and 0 <= y < col and matrix[x][y] > matrix[i][j]:
                curr = max(curr, self.dfs(matrix, x, y, cache))
        
        cache[i][j] = curr + 1    # 2
        
        return cache[i][j]
    
    # TC: O(mn)
    
    # SC: O(mn)
    
    # 1. max(max(ans)) wont return the max value of cache
    #    as max(ans) return the row in cache which has the max row[0] value
    #    e.g. if cache = [[1,4], [2, 1]], max(cache) => [2, 1]
    # 2. curr represents the longest route from the neighbors of [i][j]
    #    and current cache[i][j] is 0 as we have checked in the previous
    #    thus we have to add 1 which is the current [i][j] cell
