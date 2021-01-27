class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.helper(s) == self.helper(t)
        
    def helper(self, s):
        temp = {}
        i = 0
        l = []
        for c in s:
            if c not in temp:
                temp[c] = i
                l.append(i)
            else:
                l.append(temp[c])
            i += 1
        
        return l
    
    # TC: O(n)
    
    # SC: O(n) or O(1) if s only contains 26 chars
