class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        count = 0
        visited = set()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i,j) not in visited:
                    count += 1
                    self.bfs(grid, i, j, visited)
        return count
    
    def bfs(self, grid, i, j, visited):
        row = len(grid)
        col = len(grid[0])
        
        queue = collections.deque()
        queue.append((i,j))
        visited.add((i,j))
        
        while queue:
            x, y = queue.pop()
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for d in directions:
                a = x + d[0]
                b = y + d[1]
                if 0 <= a < row and 0 <= b < col and (a, b) not in visited \
                   and grid[a][b] == "1":
                    queue.appendleft((a, b))
                    visited.add((a, b))
                    
    # TC: O(m*n)
    # visit all elements of grid once
    
    # SC: O(min(m, n)) + O(m*n)
    # min(m,n) as the space taken by queue, O(m*n) is taken by visited
    
    # It is worthy to mention that when you iterate a matrix from any corener,
    # the length of queue is smaller or equal to min(m,n) as queue is a FIFO 
    # data structure. However, if you star from middle of the matrix, the length
    # of queue can certainly be longer than min(m,n). It can be smh like 
    # min(m, n)*3+b I think, but the dominating factor still is min(m,n).
