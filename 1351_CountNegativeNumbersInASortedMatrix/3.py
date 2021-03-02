class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        r, c, cnt = m - 1, 0, 0
        while r >= 0 and c < n:
            if grid[r][c] < 0:
                cnt += n - c
                r -= 1
            else:
                c += 1
        return cnt
    
    # TC: O(r+c)
    
    # SC: O(1)
    
    # ref: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/discuss/510249/
