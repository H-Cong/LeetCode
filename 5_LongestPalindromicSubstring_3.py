class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        length = 0
        start = 0
        
        for i in range(n):
            curr = max(self.getLen(i, i, s), self.getLen(i, i+1, s))
            if length >= curr: continue
            
            length = curr
            start = i - (curr-1) // 2
        
        return s[start: start + length]
    
    def getLen(self, l, r, s):
        n = len(s)
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
        
        return r - l - 1
    
    # TC: O(n^2)
    
    # SC: O(1)   
    
    # ref: https://www.youtube.com/watch?v=g3R-pjUNa3k&ab_channel=HuaHua
