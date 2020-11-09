class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s: return 0
        
        seen = []
        ans = 0
        
        for i in range(len(s)):
            if s[i] not in seen:
                seen.append(s[i])
                ans = max(ans, len(seen))
            else:
                seen = seen[seen.index(s[i])+1:] # remove all elements from list till the one after s[i]
                seen.append(s[i])
        
        return ans
    
    # TC: O(n^2) I think
    # O(n) for the for loop. O(n) for in list operation. O(n) for list.index() operation
    
    # SC: O(128)
    # worst case list will take in all 128 ASCII chars
