class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''
        Revert half x
        '''
        if x < 0: return False
        if x%10 == 0 and x != 0: return False
        
        half = 0
        while half < x:
            digit = x%10
            half = half*10 + digit
            x //= 10

        return half == x or half // 10 == x
    
    # TC: O(logx)
    
    # SC: O(1)
