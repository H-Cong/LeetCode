class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ans = copy.deepcopy(board)
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                count = 0
                for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1), (i+1, j+1), (i+1, j-1), (i-1, j+1), (i-1, j-1)):
                    if 0 <= x < m and 0 <= y < n and ans[x][y] == 1:
                        count += 1
                if ans[i][j] == 0:
                    if count == 3:
                        board[i][j] = 1
                else:
                    if count < 2 or count > 3:
                        board[i][j] = 0
                
    # TC: O(mn)
    
    # SC: O(mn)
    
   
        
