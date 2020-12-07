'''Life is short, use Python. LOL'''
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        '''
        Iteration
        '''
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
            
    # TC: O(n)
    
    # SC: O(1)
    
    # to finish in O(1) space, iteration is a must. If you use a recursive call
    # then the recursion stack cost will be O(n)
