class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        HashTable
        '''
        s = collections.Counter(s)
        t = collections.Counter(t)
        if s == t:
            return True
        return False
    
    # TC: O(n)
    
    # SC: O(n)
    # in this problem, if we only use lower a-z, then SC is O(1)
    # but if we use unicode char, then it is O(n)
