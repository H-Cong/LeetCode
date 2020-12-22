class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
        DP
        '''
        if not s: return None
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        ans = 0
        for i in range(n):
            dp[i][i] = True
            ans += 1
            if i + 1 < n:
                if s[i] == s[i+1]:
                    dp[i][i+1] = True
                    ans += 1
       
        for i in reversed(range(n)):
            for j in range(i+2, n):
                if dp[i+1][j-1] and s[i] == s[j]:
                    dp[i][j] = True
                    ans += 1
        
        return ans
    
    # TC: O(n^2)
    
    # SC: O(n^2)

    # why reversed i is dp[i][j] is depend on dp[i+1][j-1]
    # thus we need to first check larger i then smaller i
