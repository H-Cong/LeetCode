class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        DP
        '''
        if s[0] == '0': return 0
        dp1 = 1
        dp2 = 1 
        for i in range(1, len(s)):
            curr = 0
            if s[i] != '0': # if current digit is valid
                curr += dp2
            if '10' <= s[i-1:i+1] <= '26': # if current and previous together is valid
                curr += dp1
            dp1, dp2 = dp2, curr
        return dp2
            
            
    # TC: O(n) ??
    
    # SC: O(1)
    
    # ref: https://leetcode.com/problems/decode-ways/discuss/723609/Python-Solutions
