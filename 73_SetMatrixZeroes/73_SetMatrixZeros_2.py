class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''
        Use first row and first col as the set to store whether this row/col
        need to be set to zeros
        '''
        is_col = False
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1,col):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
                    
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for j in range(col):
                matrix[0][j] = 0
        
        if is_col:
            for i in range(row):
                matrix[i][0] = 0
                
    # TC: O(m*n)
    
    # SC: O(1)
    
    # NOTE: the order matters. 
    # we need to first set first row and col to mark 0s
    # then we LEAVE first row/col alone, then set all 0s inside matrix
    # then we go back to set first row/col to 0 if needed
    
    # ref: https://leetcode.com/problems/set-matrix-zeroes/solution/
