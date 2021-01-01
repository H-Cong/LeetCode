class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        DP: top down
        '''
        return self.LCS(0, 0, text1, text2)
    
    @lru_cache(maxsize=None)
    def LCS(self, i, j, text1, text2):
        if i == len(text1) or j == len(text2): return 0
        
        if text1[i] == text2[j]: return 1 + self.LCS(i+1, j+1, text1, text2)
        else: return max(self.LCS(i+1, j, text1, text2), self.LCS(i, j+1, text1, text2))
        
    # TC: O(m*n)
    
    # SC: O(m*n)
    
    # ref: https://leetcode.com/problems/longest-common-subsequence/solution/
    # GOLDEN SOLUTION
        
                    
