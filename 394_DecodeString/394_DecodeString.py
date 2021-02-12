class Solution:
    def decodeString(self, s: str) -> str:
        '''
        Stack
        '''
        
        stack = []
        curr = ''
        k = 0
        
        for c in s:
            if c.isdigit():
                k = k*10 + int(c)
            elif c == '[':
                stack.append((k, curr))
                curr = ''
                k = 0
            elif c == ']':
                k, last = stack.pop()
                curr = last + k*curr
                k = 0
            else:
                curr += c
        
        return curr
    
    # TC: O(maxk*n)
    # where maxK is the maximum value of k and n is the length of a given string ss. 
    # We traverse a string of size nn and iterate k times to decode each pattern of form    
    # k[string]. This gives us worst case time complexity as O(maxK⋅n).
    
    # SC: O(m+n)
    # where m is the number of letters(a-z) and n is the number of digits(0-9) in string s. 
    # In worst case, the maximum size of stack could be m+n
    
    # ref: https://leetcode.com/problems/decode-string/discuss/87662/Python-solution-using-stack


