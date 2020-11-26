class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s: return 0
        
        seen = [-1] * 128
        ans = start = 0

        for i, ch in enumerate(s):
            if seen[ord(ch)] != -1:
                start = max(start, seen[ord(ch)] + 1)
            
            ans = max(ans, i - start + 1)
            seen[ord(ch)] = i
        
        return ans
    
    # TC: O(n) 
    # O(n) for the for loop. 
    
    # SC: O(128)
    # worst case list will take all 128 ASCII char
    
    # ref: https://zxi.mytechroad.com/blog/hashtable/leetcode-3-longest-substring-without-repeating-characters/
