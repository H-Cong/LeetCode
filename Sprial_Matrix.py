class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix) # calculate # of rows
        col = len(matrix) # calculate # of columns
        if row == 0 or col == 0: # Corner case: empty matrix
            return []
        
        res = matrix[0] # First row of matrix will be always added to result for non-empty matrix
        
        if row > 1:
            for i in range(1, row): # Begin to add the last column from top to bottom. P.S. range(a, b)
                                    # will not include b
                res.append(matrix[i][col-1]) # col # stays the same, whill row # increases
                
            for j in range(col-2, -1, -1): # Begin to add the last row from right to left
                                           # col # from col-2, col-1, ..., 0. P.S. -1 not included
                res.append(matrix[row-1][j]) # row # stays the same
                
            if col > 1: # if there is only one column exists, then last column = first column, just return
                for i in range(row-2, 0, -1): # Add the first column but excluding the first and last 
                                              # element of the first column
                    res.append(matrix[i][0])
                    
        # Now we need to cut the remaining matrix into a new matrix and reuse the function
        # M = matrix[1:-1][1:-1] # Why this always gives empty array [] ???
        M = []
        for k in range(1, row-1): # Append row by row but excluding all elements that have already been 
                                  # added to the result
            M.append(matrix[k][1:-1])
            
        return res + self.spiralOrder(M)
            
        # TC and SC??? 
        # recursion的缺点就是增加了space complexity，从O(1)直接增加到O(M*N*min(M,N)) / quadruple 
        # ????
