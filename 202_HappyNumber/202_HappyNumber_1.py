class Solution:
    def isHappy(self, n: int) -> bool:
        '''
        Hashset
        '''
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.get_next(n)
        
        return n == 1
    
    def get_next(self, n):
        sum_ = 0
        while n > 0:
            n, digit = divmod(n, 10)
            sum_ += digit**2
        
        return sum_
    
    # TC: O(logn)
    
    # SC: O(logn)
    
    # ref: https://leetcode.com/problems/happy-number/solution/
