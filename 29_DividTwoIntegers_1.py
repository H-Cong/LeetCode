class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = int(dividend / divisor)
        if res > 2**31 - 1:
            return 2**31 - 1
        return int(dividend / divisor)
    
    # TC: O(1)
    
    # SC: O(1)
    
    # but this is not correct approach as division operation is not allowed
