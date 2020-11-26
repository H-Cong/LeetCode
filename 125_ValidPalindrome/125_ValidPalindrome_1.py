class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i < j:
            if not s[i].isalnum():  # .isalnum() is a func to determin whether a char is a alphabets or a number
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
                
        return i == j or i - j == 1 # or just return True 
                                    # both serve the same purpose
    
    # TC: O(n)
    # n is the length of s
    
    # SC: O(1)
