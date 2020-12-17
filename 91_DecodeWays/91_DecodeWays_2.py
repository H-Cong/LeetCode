class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        DP
        '''
        if s[0] == "0": return 0
        dp = [0]*(len(s)+1)
        dp[0], dp[1] = 1, 1
        for i in range(1, len(s)):
            if s[i] != "0":
                dp[i+1] += dp[i]
            if '10' <= s[i-1:i+1] <= '26':  
                dp[i+1] += dp[i-1]
        return dp[-1]
            
            
    # TC: O(n) ??
    
    # SC: O(n)
    
    # ref: https://leetcode.com/problems/decode-ways/discuss/30352/Accpeted-Python-DP-solution
