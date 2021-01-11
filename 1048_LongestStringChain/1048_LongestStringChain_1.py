class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        '''
        DP
        '''
        dp = {}
        res = 1
        
        for word in sorted(words, key=len):
            dp[word] = 1
            for i in range(len(word)):
                prev = word[:i] + word[i+1:]
                if prev in dp:
                    dp[word] = max(dp[word], dp[prev]+1)
                    res = max(res, dp[word])
        
        return res
    
    # TC: O(nlogn + n*l^2)
    # n is number of words, l is average length of word in words
    # nlogn for sort(), n for for loop, l for inner for loop, l for slicing
    
    # SC: O(n*l)
    
    # ref: https://leetcode.com/problems/longest-string-chain/discuss/294890/C%2B%2BJavaPython-DP-Solution
