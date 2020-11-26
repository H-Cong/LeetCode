class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31-1
        halfMin = -2**30
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
            powerOfTwo = 1
            value = divisor
            while value >= halfMin and value + value >= dividend:
                powerOfTwo += powerOfTwo
                value += value
            res += powerOfTwo
            dividend -= value
            
        
        return -res if isNeg == 1 else res
    
    # TC: O((logn)^2)
    # in the worst case, we have O(logn) searches with each search taking O(logn) time. 
    # This gives us O((logn)⋅(logn))=O((logn)^2) as our total time complexity.
    
    # SC: O(1)
    
    # ref: leetcode solution is a very nicely written article
