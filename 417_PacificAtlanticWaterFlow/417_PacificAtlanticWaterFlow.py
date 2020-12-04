class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        '''
        DFS
        '''
        if not matrix or not matrix[0]: return None
        
        row = len(matrix)
        col = len(matrix[0])
        
        p_connected = set()
        a_connected = set()
        
        ans = []
        
        for i in range(row):
            self.dfs(matrix, i, 0, p_connected)
            self.dfs(matrix, i, col-1, a_connected)
        
        for j in range(col):
            self.dfs(matrix, 0, j, p_connected)
            self.dfs(matrix, row-1, j, a_connected)
            
        for i in range(row):
            for j in range(col):
                if (i, j) in p_connected and (i, j) in a_connected:
                    ans.append([i,j])
        
        return ans
    
    def dfs(self, matrix, i, j, visited):
        visited.add((i, j))
        row, col = len(matrix), len(matrix[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for d in directions:
            x, y = i + d[0], j + d[1]
            if x < 0 or x >= row or y < 0 or y >= col or (x, y) in visited or matrix[x][y] < matrix[i][j]: # 1
                continue
            self.dfs(matrix, x, y, visited)
            
    # TC: O(m*n)
    # since we keep a visited set for each ocean, we only visit a cell if 
    # it is not visited before. For each ocean, the worst case is mn thus totally O(mn)
    
    # SC: O(2mn + h) = O(mn)
    # For each DFS we need O(h) space used by the system stack, 
    # where h is the maximum depth of the recursion. In the worst case, O(h) = O(m*n)
    # Each visited set can have at maximum all cells from the matrix so O(mn). Two ocean means O(2mn)
    
    # 1. Remember, (i, j) is connected, meaning from this [i][j] position we can reach to a ocean
    #    Thus, if its neighbour wants to reach the same ocean through the [i][j] cell, it needs to
    #    have a higher or equal height of matrix[i][j]
    
    # ref: https://leetcode.com/problems/pacific-atlantic-water-flow/discuss/90739/Python-DFS-bests-85.-Tips-for-all-DFS-in-matrix-question.
    # ref2: https://leetcode.com/problems/pacific-atlantic-water-flow/discuss/438276/Python-beats-98.-DFS-template-for-Matrix
