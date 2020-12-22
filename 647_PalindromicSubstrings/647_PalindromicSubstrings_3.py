class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
        Expand from center
        '''
        if not s: return 0
        ans = 0
        for i in range(len(s)):
            ans += self.helper(s, i, i)
            ans += self.helper(s, i, i+1)
        
        return ans
    
    def helper(self, s, l, r):
        cnt = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            cnt += 1
            l -= 1
            r += 1
        
        return cnt
    
    # TC: O(n^2) where n is len(s)
    # The number of possible palindromic centers is 2n−1: 
    # there are n single character centers and n-1 consecutive character pairs as centers.
    # Each center can potentially expand to the length of the string, 
    # so time spent on each center is linear on average. 
    # Thus total time spent is n(2n-1) ~ n^2
    
    # SC: O(1)
