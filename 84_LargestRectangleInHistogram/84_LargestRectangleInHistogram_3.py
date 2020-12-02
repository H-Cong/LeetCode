class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        Stack
        '''
        if not heights: return 0
        
        heights.append(0)
        stack = [-1]
        ans = 0
        n = len(heights)
        
        for i in range(n):
            while heights[stack[-1]] > heights[i]: # 1
                h = heights[stack.pop()]
                w = i - stack[-1] - 1              # 2
                ans = max(ans, h*w)
            stack.append(i)
        
        heights.pop()                              # 3
            
        return ans
    
    # TC: O(n)
    
    # SC: O(n)
    
    # 1. As 0 has been appended to heights, and there is only non-negatives in heights
    #    thus i = 0 has been taken care of. As heights[0] >= 0 = heights[-1].
    # 2. Note, since stack has been popped in last step, here stack[-1] is the index of 
    #    the height prior to h
    # 3. This is a good practice to revert heights to its original status. Though this 
    #    step will not affect the result.

    # ref: https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/28917/AC-Python-clean-solution-using-stack-76ms
