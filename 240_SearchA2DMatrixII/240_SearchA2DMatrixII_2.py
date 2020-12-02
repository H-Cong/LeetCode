class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        Search Space Reduction
        '''
        if not matrix or not matrix[0]: return False
        m = len(matrix)
        n = len(matrix[0])
        
        # start from left bottom
        row = m - 1
        col = 0
        
        while row >=0 and col < n:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else:
                return True
        
        return False
    
    # TC: O(m + n)
    
    # SC: O(1)
        
