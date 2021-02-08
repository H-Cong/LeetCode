class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'AEIOUaeiou'
        temp = []
        for i, c in enumerate(s):
            if c in vowels:
                temp.append(c)
        
        res = ''
        for c in s:
            if c in vowels:
                res += temp[-1]
                temp.pop()
            else:
                res += c
        
        return res
    
    # TC: O(n)
    
    # SC: O(n)
    
    # pop() is O(1) for the last element
        
        
