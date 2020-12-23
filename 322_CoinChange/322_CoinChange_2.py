class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        DP BottomUp
        '''
        dp = [float('inf')]*(amount+1)
        dp[0] = 0 # there is one way to make 0 amount by providing 0 coins
        
        for i in range(1, amount+1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i-c] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1
    
    # TC: O(a*c) where a is amount and c is number of coins
    # two for loops
    
    # SC: O(a)
    # dp list
