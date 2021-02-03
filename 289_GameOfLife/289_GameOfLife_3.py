class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                count = 0
                for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1), (i+1, j+1), (i+1, j-1), (i-1, j+1), (i-1, j-1)):
                    if 0 <= x < m and 0 <= y < n and abs(board[x][y]) == 1: # NOTE THE abs() here
                        count += 1
                if board[i][j] == 0:
                    if count == 3:
                        board[i][j] = 2
                else:
                    if count < 2 or count > 3:
                        board[i][j] = -1
        
        for i in range(m):
            for j in range(n):
                if board[i][j] <= 0:
                    board[i][j] = 0
                else:
                    board[i][j] = 1
                
    # TC: O(mn)
    
    # SC: O(1)

    # If we have an extremely sparse matrix, it would make much more sense to actually save the location of only the live cells 
    # and then apply the 4 rules accordingly using only these live cells.

    # However, when the entire board cannot fit into memory. we assume that the contents of the matrix are stored in a file,
    # one row at a time. In order for us to update a particular cell, we only have to look at its 8 neighbors which essentially
    # lie in the row above and below it. So, for updating the cells of a row, we just need the row above and the row below. 
    # Thus, we read one row at a time from the file and at max we will have 3 rows in memory. 
    
