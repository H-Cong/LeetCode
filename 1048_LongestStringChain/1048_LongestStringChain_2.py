class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        '''
        DFS with memoization
        '''
        def dfs(word):
            if word not in dp:
                return 0
            if not dp[word]:
                dp[word] = max([dfs(word[:i]+word[i+1:]) + 1 for i in range(len(word))])
            return dp[word]
			
        dp = {word: None for word in words}
        return max([dfs(word) for word in dp if not dp[word]])
    
    # TC: O(n*l^2)
    # n is number of words, l is average length of word in words
    # nlogn for sort(), n for for loop, l for inner for loop, l for slicing
    
    # SC: O(n*l)
    
    # ref: https://leetcode.com/problems/longest-string-chain/discuss/483103/Python-8-lines-DFS-with-memoization
