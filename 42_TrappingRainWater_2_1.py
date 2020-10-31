class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 2:
            return 0
        
        water = 0
        
        # assign left/right to 0 if i is the leftmost or rightmost index
        for i in range(len(height)):
            left = max(height[:i]) if height[:i] else 0 # or "if i != 0"
            right = max(height[i:]) if height[i:] else 0 # or "if i != len(height) - 1"
            water += max(min(left, right) - height[i], 0)
        
        return water
        
        # TC: O(n^2)
        # We iterate each element in array, takes O(n)
        # For each element of array, we iterate the left and right parts, takes O(n)
        
        # SC: O(1)
        # Only constant space required for left, right.
