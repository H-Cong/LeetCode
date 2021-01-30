class Solution:
    def numSquares(self, n: int) -> int:
        '''
        DP bottom up
        '''
        squares = [i**2 for i in range(0, int(math.sqrt(n)) + 1)]
        dp = [float('inf')] * (n + 1)
        dp[0] = 0 # bottom case
        
        for i in range(1, n+1):
            for square in squares:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i-square] + 1)
        
        return dp[-1]
    
    # TC: O(n*sqrt(n))
    # xn main step, we have a nested loop, where the outer loop is of 
    # n iterations and in the inner loop it takes at maximum sqrt(n) iterations.
    
    # SC: O(n)
    # We keep all the intermediate sub-solutions in the array dp[].
    
    # ref: https://leetcode.com/problems/perfect-squares/solution/
