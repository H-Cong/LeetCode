class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        Binary Search
        '''
        l = 0
        r = x
        while l <= r:
            m = l + (r - l) // 2
            if m * m > x:
                r = m - 1
            else:
                l = m + 1
            
        return r
    
    # TC: O(log(r-l)) = O(logx)
    
    # SC: O(1)
    
    # why return r? because r is the first number that the square of 
    # this number is smaller or equal to x
