class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r, m = list(ransomNote), list(magazine)
        r1, m1 = collections.Counter(r), collections.Counter(m)
        for k in r1.keys():
            if k not in m1: return False
            if r1[k] > m1[k]: return False
        return True
    
    # TC: O(n) where n is the shorter string length
    
    # SC: O(k) 
    # k is 26 in this case maximum, thus it is also O(1)
