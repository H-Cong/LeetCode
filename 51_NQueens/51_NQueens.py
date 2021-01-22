class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        '''
        DFS
        '''
        result = self.dfs([], [], [], [], n)
        return [['.'* i + 'Q' + '.'*(n-i-1) for i in sol] for sol in result]
    
    def dfs(self, result, queens, dif_, sum_, n):
        row = len(queens)
        if row == n:
            result.append(queens)
            return
            
        
        for col in range(n):
            if col not in queens and row - col not in dif_ and row + col not in sum_:
                self.dfs(result, queens + [col], dif_ + [row - col], sum_ + [row + col], n)
        
        return result
    
    # TC: O(n!)
    # There is N possibilities to put the first queen, not more than 
    # N (N - 2) to put the second one, not more than N(N - 2)(N - 4) 
    # for the third one etc. In total that results in O(N!) time complexity.
    
    # SC: O(n)
    # O(N) to keep an information about diagonals and rows.

    # ref: https://leetcode.com/problems/n-queens/discuss/19810/
    
    # Basically since all slopes are either (-1) or (1) going up or down 
    # (we only care about 45/135 degree slopes, we are bascially taking a coord and 
    # solving for the y intercept in the slop intercept for y = mx + b. 
    # This always transforms into two forms in our case since we have two slopes. 
    # EITHER: y = (-1)x + b -> y = -x + b -> y + x = b OR y = 1x + b -> y = x + b -> y - x = b. 
    # So either on the up or down slope you solve for where a point on this line would intercept 
    # the y axis. Something to note is even though a slope looks like its going downward in a 
    # visual image of a 2d grid, you need to check if the indices are actually increasing, 
    # in programming we usually draw our grids backwards where the y axis value increases as it grows
    # downward. This could cause you to assume the wrong slope. Anyway, you plug the slope and 
    # coord for your point in y = mx + b the result will be b = (some value). That is the y 
    # intercept and it will be consistent across any point on the same line so you can tell 
    # in constant time via a lookup table if any other queens have been placed on this line.
                
