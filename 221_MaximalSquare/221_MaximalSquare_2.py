class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        '''
        DP
        '''
        if not matrix or not len(matrix): return 0
        row = len(matrix)
        col = len(matrix[0])
        dp = [0] * (col+1) # NOTE: dp is 1 col bigger than matrix
        maxLen = 0
        prev = 0
        
        for i in range(1, row+1): # NOTE here is row + 1 as well
            for j in range(1, col+1):
                temp = dp[j]
                if matrix[i-1][j-1] == '1':
                    dp[j] = min(dp[j], prev, dp[j-1]) + 1
                    maxLen = max(maxLen, dp[j])
                else:
                    dp[j] = 0
                prev = temp
        
        return maxLen**2
    
    # TC: O(row*col)
    
    # SC: O(col)
    
    # ref: https://leetcode.com/problems/maximal-square/solution/
