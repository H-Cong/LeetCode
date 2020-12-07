class Solution:
    def reverse(self, x: int) -> int:
        '''
        String
        '''
        neg = False
        if x < 0: 
            x = -x
            neg = True
            
        s = list(str(x))
        s = s[::-1]
        
        if neg:
            res = -int("".join(s))
        else:
            res = int("".join(s))
        
        if res > 2**31 - 1 or res < -2**31:
                return 0
        
        return res
    
    # TC: O(x)
    # list(str) O(n); [::-1] O(n); .join() O(n)
    
    # SC: O(x)
    # O(n) for s
