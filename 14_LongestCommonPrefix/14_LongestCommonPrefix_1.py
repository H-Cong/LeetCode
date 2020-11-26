class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Horizontal Scan
        if not strs: return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0: # == 0 means prefix exists at beginning of strs[i]
                prefix = prefix[:-1] # tram prefix from right side one char at a time
            if not prefix:
                return ""
        return prefix
    
    # TC: O(S), where S is the sum of all characters in all strings
    # In the worst case all nn strings are the same. The algorithm compares 
    # the string S1 with the other strings [S_2...S_n][S There are S character 
    # comparisons, where S is the sum of all characters in the input array.
    
    # SC: O(1)
