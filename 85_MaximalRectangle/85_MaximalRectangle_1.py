class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        '''
        DP
        '''
        if not matrix: return 0
        m = len(matrix)
        n = len(matrix[0])
        
        left = [0] * n
        right = [n] * n
        height = [0] * n
        
        ans = 0
        
        for i in range(m):
            curr_l, curr_r = 0, n
            for j in reversed(range(n)):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], curr_r)
                else:
                    right[j] = n
                    curr_r = j
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                    left[j] = max(left[j], curr_l)
                else:
                    height[j] = 0
                    left[j] = 0
                    curr_l = j + 1
                ans = max(ans, height[j]*(right[j]-left[j]))
            
        return ans
    
    # TC: O(row*col)
    
    # SC: O(col)
    
    # ref: https://leetcode.com/problems/maximal-rectangle/discuss/29054/Share-my-DP-solution
