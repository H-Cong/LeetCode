class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s
        n = len(s)
        dp = [[False]*n for i in range(n)]
        # DONT use dp = [[False]*n]*n
        # ref: https://stackoverflow.com/questions/2397141/how-to-initialize-a-two-dimensional-array-in-python
        
        for i in range(n):
            dp[i][i] = True
        
        ans = s[0]
        for j in range(n):
            for i in range(j): # here i = j is excluded as it has already be set to True. And i = j can cause out of index error when i = n-1
                if s[i] == s[j] and (j-i < 2 or dp[i+1][j-1]): 
                # j-i < 2 to deal with when i and j are next to each other
                    dp[i][j] = True
                    if j - i + 1 > len(ans): # this statement cannot be put in the above if statement
                                             # for early termination as it will block the dp matrix to set to True 
                        ans = s[i:j+1]
        
        return ans
    
    # TC: O(n^2)
    
    # SC: O(n^2)

    # ref: https://www.youtube.com/watch?v=ZnzvU03HtYk
