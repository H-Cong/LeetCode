"""
dp is a list to store whether any substring can be broke by the words in wordDict
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True                              # 1
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:  # 2
                    dp[i] = True
                    break
                
        return dp[-1]
    
    # TC: O(n^3)
    # two layers of O(n) for loop. Slicing is also a O(n) function
    
    # SC: O(n)
    
    # 1. dp[0] refers to empty string, i.e. "". This sets to True bc for any i,
    #    j serves as a break point for s[0:i]. When j = 0, we need to make sure
    #    that this s[j:i] in wordDict will still be checked.
    # 2. As slicing [j:i] wont include ith position. In order to make sure 
    #    the whole s string will also be checked in this if statement, we need 
    #    i be able to reach the length of whole s in the outer for loop.
