class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31-1
        # change both numbers to negative
        isNeg = 0
        if dividend > 0:
            isNeg += 1
            dividend = -dividend
        if divisor > 0:
            isNeg += 1
            divisor = -divisor
        
        res = 0
        while divisor >= dividend:
            dividend -= divisor
            res += 1
        
        return -res if isNeg == 1 else res
    
    # TC: O(n)
    
    # SC: O(1)
    
    # this can work but it raises a TLE error
    # as it is too slow when divisor = 1 or -1 and dividend is a very large number
    # e.g. Min_Int or Max_Int
