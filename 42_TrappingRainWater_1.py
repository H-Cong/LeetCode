class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 2:
            return 0
        
        water = 0
        left, right = 0, len(height)-1
        max_l, max_r = 0, 0
        
        while left < right:
            if height[left] < height[right]:
                if height[left] >= max_l:
                    max_l = height[left]
                else:
                    water += max_l - height[left]
                left += 1
        
            else:
                if height[right] >= max_r:
                    max_r = height[right]
                else:
                    water += max_r - height[right]
                right -= 1
        
        return water
        
        # TC: O(n)
        # Single iteration of n
        
        # SC: O(1)
        # Only constant space required for left, right, left_max and right_max.
