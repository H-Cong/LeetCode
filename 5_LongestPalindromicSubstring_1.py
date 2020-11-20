class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s
        candidates = []
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if s[i:j+1] not in candidates:
                    candidates.append(s[i:j+1])
        # print(candidates)
        
        deleted = []
        
        for i in range(len(candidates)):
            l, r = 0, len(candidates[i])-1
            while l < r:
                if candidates[i][l] == candidates[i][r]:
                    l += 1
                    r -= 1
                else:
                    deleted.append(candidates[i])
                    break
        
        for item in deleted:
            candidates.remove(item)
            
        res = s[0]
        
        for candidate in candidates:
            if len(candidate) > len(res):
                res = candidate
    
        return res
    
    # TC: O(n^3)
    # this comes from the second for loop
    # as the total number of substring is (n+1)*n/2, and inner while loop is O(n)
    
    # SC: O(n^2)
    # this comes from the candidates list
    
    # this approach is a naive brute force one, which raises TLE error. 
    # and the code above can be totally cleaned to make SC to O(1) by putting the comparison
    # step directly into the first for loop. I think. 
