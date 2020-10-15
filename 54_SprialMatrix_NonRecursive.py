class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Non recursive solution
        res = []
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return res
        
        # 4 index
        top, bottom, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
        
        while top <= bottom and left <= right:
            for i in range(left, right+1):
                res.append(matrix[top][i])
            top += 1
            
            for j in range(top, bottom+1):
                res.append(matrix[j][right])
            right -= 1
            
            if top <= bottom:
                for i in range(right, left-1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1
                
            
            if left <= right:
                for i in range(bottom, top-1, -1):
                    res.append(matrix[i][left])
                left += 1
        
        return res
        
        # TC log(m*n) = log(N)
        # SC log(N)
                    
