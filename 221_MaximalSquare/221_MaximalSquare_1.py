class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        '''
        DP Similar: 85
        '''
        if not matrix or not len(matrix): return 0
        row = len(matrix)
        col = len(matrix[0])
        dp = [[0] * (col+1) for _ in range(row+1)] # NOTE: dp is 1 row&col bigger than matrix
        maxLen = 0
        
        for i in range(1, row+1): # NOTE here is row + 1 as well
            for j in range(1, col+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j], min(dp[i-1][j-1], dp[i][j-1])) + 1
                    maxLen = max(maxLen, dp[i][j])
        
        return maxLen**2
    
    # TC: O(row*col)
    
    # SC: O(row*col)
    
    # ref: https://leetcode.com/problems/maximal-square/solution/
