class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s: return 0
        
        seen = [0] * 128
        start = ans = 0
        
        for i, c in enumerate(s):
            seen[ord(c)] += 1
            while seen[ord(c)] > 1:
                seen[ord(s[start])] -= 1
                start +=1 
            ans = max(ans, i - start + 1)
        
        return ans
    
    # TC: O(n) ??
    # O(n) for the for loop. 
    
    # SC: O(128)
    # worst case list will take all 128 ASCII char
    
    # ref: youtube.com/watch?v=EbemoR4LooA&ab_channel=山景城一姐
