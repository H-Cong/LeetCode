class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        DP
        '''
        d = [[1]*n for _ in range(m)]
        
        for i in range(1, m):
            for j in range(1, n):
                d[i][j] = d[i-1][j] + d[i][j-1]
        
        return d[-1][-1]
    
    # TC: O(m*n)
    
    # SC: O(m*n)
    
    # ref: https://leetcode.com/problems/unique-paths/solution/
