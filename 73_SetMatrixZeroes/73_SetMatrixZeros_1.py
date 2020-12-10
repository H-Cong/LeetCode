class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = set()
        c = set()
        
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    r.add(i)
                    c.add(j)
        
        for i in r:
            for j in range(col):
                matrix[i][j] = 0
        for i in range(row):
            for j in c:
                matrix[i][j] = 0
                
    
    # TC: O(m*n)
    
    # SC: O(m + n)
