class Solution:
    def isHappy(self, n: int) -> bool:
        '''
        Hashset
        '''
        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum([int(d)**2 for d in str(n)])
        
        return n == 1
    
    # TC: O(logn)
    
    # SC: O(logn)
    
    # ref: https://leetcode.com/problems/happy-number/discuss/56915/My-Python-Solution
