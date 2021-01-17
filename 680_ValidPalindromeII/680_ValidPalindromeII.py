class Solution:
    def validPalindrome(self, s: str) -> bool:
        '''
        Two pointers
        '''
        l = 0
        r = len(s)-1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                temp_l = s[:l] + s[l+1:]
                temp_r = s[:r] + s[r+1:]
                return temp_l == temp_l[::-1] or temp_r == temp_r[::-1]
        return True
    
    # TC: O(n)
    
    # SC: O(1)
            
