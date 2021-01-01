class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        DP: top down
        '''
        return self.LCS(0, 0, text1, text2, {})
        
    
    def LCS(self, i, j, text1, text2, cache):
        if (i,j) in cache: return cache[(i, j)]
        if i == len(text1) or j == len(text2): return 0
        
        if text1[i] == text2[j]: cache[(i, j)] = 1 + self.LCS(i+1, j+1, text1, text2, cache)
        else: cache[(i, j)] = max(self.LCS(i+1, j, text1, text2, cache), self.LCS(i, j+1, text1, text2, cache))
        
        return cache[(i, j)]
        
    # TC: O(m*n)
    
    # SC: O(m*n)
    
    # ref: https://leetcode.com/problems/longest-common-subsequence/solution/
    # GOLDEN SOLUTION
    # ref: https://leetcode.com/problems/longest-common-subsequence/discuss/862562/progression-of-python-solutions
