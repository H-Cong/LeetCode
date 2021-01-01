class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        DP: buttom up
        '''
        if len(text2) < len(text1):
            text1, text2 = text2, text1
        
        prev = [0] * (len(text1)+1) 
        curr = [0] * (len(text1)+1) 
        
        for col in reversed(range(len(text2))):
            for row in reversed(range(len(text1))):
                if text2[col] == text1[row]:
                    curr[row] = 1 + prev[row+1]
                else:
                    curr[row] = max(curr[row+1], prev[row])
            prev, curr = curr, prev
        
        return prev[0]
        
    # TC: O(m*n)
    
    # SC: O(min(m, n))
    
    # ref: https://leetcode.com/problems/longest-common-subsequence/solution/
    # GOLDEN SOLUTION
                    
