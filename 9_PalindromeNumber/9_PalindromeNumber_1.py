class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''
        Using list
        '''
        if x < 0: return False
        if x%10 == 0 and x != 0: return False
        
        stack = []
        while x != 0:
            digit = x%10
            stack.append(digit)
            x //= 10

        l, r = 0, len(stack)-1
        while l < r:
            if stack[l] != stack[r]:
                return False
            l += 1
            r -= 1
        
        return True
    
    # TC: O(logx)
    
    # SC: O(x)
            
