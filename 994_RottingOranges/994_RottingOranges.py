class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        BFS
        '''
        if not grid or not grid[0]: return -1
        
        queue = collections.deque()
        fresh_orange = 0
        row, col = len(grid), len(grid[0])
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh_orange += 1
        
        ans = 0 
        while queue and fresh_orange:
            ans += 1
            for _ in range(len(queue)): # NOTE
                r, c = queue.popleft()
                directions = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
                for x, y in directions:
                    if 0 <= x < row and 0 <= y < col and grid[x][y] == 1:
                        grid[x][y] = 2
                        fresh_orange -= 1
                        queue.append((x, y))
        
        return ans if fresh_orange == 0 else -1
    
    # TC: O(r*c)
    
    # SC: O(r*c)
    
    # NOTE: the queue.append() operation wont affect the len(queue) of current level
    
    # ref: https://leetcode.com/problems/rotting-oranges/discuss/563686/
