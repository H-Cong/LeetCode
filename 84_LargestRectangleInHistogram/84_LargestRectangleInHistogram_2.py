class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        Stack
        '''
        if not heights: return 0
        
        stack = [-1]
        ans = 0
        n = len(heights)
        
        for i in range(n):
            if i == 0:
                stack.append(i)
                ans = heights[0]
                continue
            while stack[-1] != -1 and heights[stack[-1]] > heights[i]:
                h = heights[stack[-1]]
                stack.pop()
                w = i - stack[-1] -1
                ans = max(ans, h*w)
            stack.append(i)
            
        while stack[-1] != -1:           # 1
            h = heights[stack[-1]]
            stack.pop()
            w = n - stack[-1] -1
            ans = max(ans, h*w)
            
        return ans
    
    # TC: O(n)
    
    # SC: O(n)
    
    # 1. this is to deal with when there are still idx left in stack
    # e.g. heights = [1,1,1,1]

    # ref: LeetCode Official Solution
