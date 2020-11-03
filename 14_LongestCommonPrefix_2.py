class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Vertical Scan
        if not strs: return ""
        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if i > len(strs[j]) - 1 or c != strs[j][i]:
                    return strs[0][:i]
        
        return strs[0]
    
    # TC: O(S), where S is the sum of all characters in all strings
    # In the worst case there will be n equal strings with length m and the algorithm performs 
    # S = m*n character comparisons. Even though the worst case is still the same as Horizontal
    # Scan, in the best case there are at most n*min(len) comparisons where min(len) is the length
    # of the shortest string in the array
    
    # SC: O(1)
