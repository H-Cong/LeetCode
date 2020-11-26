def isValid(self, s: str) -> bool:
        # if s[0] == ')' or s[0] == ']' or s[0] == '}':
        #     return False
        
        res = []
        
        bracket_map = {')':'(', ']':'[', '}':'{'}
        
        for char in s:
            if not res:
                res.append(char)
                continue
            if char in bracket_map:
                last = res.pop()
                if last != bracket_map[char]:
                    return False
            else:
                res.append(char)
        
        return len(res) == 0
    
    # TC: O(n)
    # because we simply traverse the given string one character at a time and append and pop operations on a list take O(1) time.
    
    # SC: O(n)
    # in worst case, we will append every char into the list
