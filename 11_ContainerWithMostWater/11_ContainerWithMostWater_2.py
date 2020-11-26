class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        l, r = 0, len(height)-1
        while l < r:
            area = max(area, min(height[l], height[r]) * (r-l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            
        return area
    
    # the core idea is that we always need to change the lower height to get a potential larger volume
    # as the width of the container is constantly decreasing
    
    # TC: O(n)
    # single while loop
    
    # SC: O(1)
    # constant space is used
