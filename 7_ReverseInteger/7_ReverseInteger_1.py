class Solution:
    def reverse(self, x: int) -> int:
        '''
        Recursion
        '''
        neg = False
        if x < 0: 
            x = -x
            neg = True
            
        res = 0
        
        while x != 0:
            res = res*10 + x%10
            x //= 10
        
        if res < -2**31 or res > 2**31 - 1:
            return 0
        
        if neg: return -res
        
        return res
    
    # TC: O(logx)
   
    # SC: O(1)
    
