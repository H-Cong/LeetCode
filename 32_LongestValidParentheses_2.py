class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l,r = 0,0
        max_ = 0
        for i in range(len(s)):
            if s[i] == '(':
                l +=1
            else:
                r +=1
            if l == r:
                max_ = max(max_, 2 * r)
            else:
                if r > l:
                    l = r = 0
        l,r = 0,0
        for i in range(len(s)-1,-1,-1):
            if s[i] == '(':
                l += 1
            else:
                r += 1
            if l == r:
                max_ = max(max_, 2 * l)
            else:
                if l > r:
                    l = r = 0
        return max_
            
        # TC: O(n)
        # n is the length of the given string.
        
        # SC: O(1)
        # Only two extra variables left and right are needed.
        
        """
        Why traverse from both directions:
        an example for you: "()(()()". Traversing from left to right yields answer 2, 
        [as left is always > right], and traversing backward yields answer 4.
        """
