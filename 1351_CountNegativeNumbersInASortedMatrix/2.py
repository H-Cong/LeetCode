class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return None
        r, c = len(grid), len(grid[0])
        ans = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] < 0:
                    ans += (c - j) * (r - i)
                    c = j
                    break
        
        return ans
    
    # TC: O(r*c)
    
    # SC: O(1)
    
    # ref: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/discuss/510249/
