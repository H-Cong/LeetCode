class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
        DP
        '''
        if not s: return None
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        ans = 0
        
        for i in reversed(range(n)):
            for j in range(i, n):
                if j - i < 2 and s[i] == s[j]:
                    dp[i][j] = True
                    ans += 1
                elif dp[i+1][j-1] and s[i] == s[j]:
                    dp[i][j] = True
                    ans += 1
        
        return ans
    
    # TC: O(n^2)
    
    # SC: O(n^2)
