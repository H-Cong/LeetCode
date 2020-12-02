class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        Brute Force
        '''
        if not heights: return 0
        
        n = len(heights)
        
        ans = 0
        
        for i in range(n):
            min_h = float('inf')
            for j in range(i, n):
                min_h = min(min_h, heights[j])
                ans = max(ans, min_h*(j-i+1))
        
        return ans
    
    # TC: O(n^2)
    
    # SC: O(1)

    # TLE
