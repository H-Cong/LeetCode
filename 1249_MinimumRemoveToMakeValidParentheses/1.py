class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        '''
        Stack
        '''
        idx_to_remove = set()
        stack = []
        for i, c in enumerate(s):
            if c not in "()": continue
            if c == "(": stack.append(i)
            elif not stack: idx_to_remove.add(i)
            else: stack.pop()
        
        idx_to_remove = idx_to_remove.union(set(stack))
        res = []
        for i, c in enumerate(s):
            if i not in idx_to_remove:
                res.append(c)
        
        return "".join(res)
    
    # TC: O(n) n is the length of the input string
    
    # SC: O(n)
    
    # ref: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/solution/
