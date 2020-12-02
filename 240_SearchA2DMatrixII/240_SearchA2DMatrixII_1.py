class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        Binary Search
        '''
        if not matrix: return False
        row = len(matrix)
        col = len(matrix[0])
       
        # search for left boundary
        l, r = 0, col - 1
        while l <= r:
            mid = l + (r - l) // 2
            if matrix[0][mid] < target:
                l = mid + 1
            elif matrix[0][mid] > target:
                r = mid - 1
            else: 
                return True
        
        # search for bottom boundary
        t, b = 0, row - 1
        while t <= b:
            mid = t + (b - t) // 2
            if matrix[mid][0] < target:
                t = mid + 1
            elif matrix[mid][0] > target:
                b = mid - 1
            else:
                return True
       
       if l < t:
            for i in range(l):
                start, end = 0, t - 1
                while start <= end:
                    mid = start + (end - start) // 2
                    if matrix[mid][i] > target:
                        end = mid - 1
                    elif matrix[mid][i] < target:
                        start = mid + 1
                    else:
                        return True
        else:
            for i in range(t):
                start, end = 0, l - 1
                while start <= end:
                    mid = start + (end - start) // 2
                    if matrix[i][mid] > target:
                        end = mid - 1
                    elif matrix[i][mid] < target:
                        start = mid + 1
                    else:
                        return True
        return False
    
    # TC: O(nlogm) where n and m are either row or col and n <= m
    
    # SC: O(1)
    
    # theoritically you can do a binary search along each row or column. 
    # this is a O(nlogm)
    # but i guess choose whichever is longer as the binary search target will
    # be the most efficient complexity
        
        
