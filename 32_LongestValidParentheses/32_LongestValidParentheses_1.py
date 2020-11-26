class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s or len(s) < 2:
            return 0
        _max = 0
        stack = []
        leftmost = -1
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                if not stack:
                    leftmost = i
                else:
                    stack.pop()
                    if not stack:
                        _max = max(_max, i-leftmost)
                    else:
                        _max = max(_max, i-stack[-1])
        
        return _max
            
        # TC: O(n)
        # n is the length of the given string.
        
        # SC: O(n)
        # The size of the stack can go up to n.
        
        # ref: https://www.youtube.com/watch?v=M1Vw5Tk1rw4
