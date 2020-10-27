class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        for i in range (len(height)):
            for j in range (i+1, len(height)):
                area = max(area, min(height[i], height[j]) * (j-i))
            
        return area
    
    # this brute force solution gives a TLE, while the JAVA brute force can be accepted
    # In terms of speed, Java is faster than Python as it is a compiled language.
    # As an interpreted language, Python has simpler, more concise syntax than Java.
    
    # TC: O(n^2)
    # two for loops
    
    # SC: O(1)
    # constant space is used
