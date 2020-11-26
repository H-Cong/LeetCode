class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 2:
            return 0
        
        water = 0
        # As the leftmost item and rightmost item will not hold water
        # we iterate from index 1 to index len(height)-2
        for i in range(1, len(height)-1):
            left = max(height[:i])
            right = max(height[i:])
            water += max(min(left, right) - height[i], 0)
        
        return water
        
        # TC: O(n^2)
        # We iterate each element in array, takes O(n)
        # For each element of array, we iterate the left and right parts, takes O(n)
        
        # SC: O(1)
        # Only constant space required for left, right.
