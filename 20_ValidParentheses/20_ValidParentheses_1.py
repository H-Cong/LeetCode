class Solution:
    def isValid(self, s: str) -> bool:
        
        res = []
        
        for char in s:
            if not res:
                res.append(char)
                continue
            if char == ')' and res[-1] == '(':
                res.pop()
            elif char == ']' and res[-1] == '[':
                res.pop()
            elif char == '}' and res[-1] == '{':
                res.pop()
            else:
                res.append(char)
        
        return len(res) == 0
    
    # TC: O(n)
    # because we simply traverse the given string one character at a time and append and pop operations on a list take O(1) time.
    
    # SC: O(n)
    # in worst case, we will append every char into the list
                
