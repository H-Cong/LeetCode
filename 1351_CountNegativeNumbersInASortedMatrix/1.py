class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return None
        r, c = len(grid), len(grid[0])
        ans = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] < 0:
                    ans += c - j
                    break
        
        return ans

    # TC: O(r*c)

    # SC: O(1)
