class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s: return 0
        
        seen = {}
        ans = start = 0
        
        for i, c in enumerate(s):
            if c in seen and start <= seen[c]:
                start = seen[c] + 1
            else:
                ans = max(ans, i - start + 1)

            seen[c] = i

        return ans
    
    # TC: O(n) 
    # O(n) for the for loop. 
    
    # SC: O(128)
    # worst case list will take all 128 ASCII char
    
