class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        '''
        Two pointers
        '''
        
        if start.count('X') != end.count('X'): # no need to check the count for 'L' and 'R'
            return False
        
        n = len(start)
        i = j = 0
        
        while i < n and j < n: # this has to be an 'and' as if i or j is out of range, index OOR error happens
            if start[i] == 'X': 
                i += 1
                continue
            if end[j] == 'X':
                j += 1
                continue
            
            if start[i] != end[j]: return False
            
            if start[i] == 'L' and i < j: return False
            
            if start[i] == 'R' and i > j:  return False
            
            i += 1
            j += 1
        
        return True
    
    # TC: O(n)
    # .count() is a O(n). Plus we only scan string once.
    
    # SC: O(1)
    
    # ref: https://leetcode.com/problems/swap-adjacent-in-lr-string/discuss/953911/Explained-Python-simple-and-concise-solution
