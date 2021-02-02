class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        '''
        BFS: start from each door
        '''
        if not rooms or not rooms[0]: return None
        m, n = len(rooms), len(rooms[0])
        doors = [(i, j) for i in range(m) for j in range(n) if not rooms[i][j]]
        for i, j in doors:
            for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if 0 <= x < m and 0 <= y < n and rooms[x][y] == 2**31 - 1:
                    rooms[x][y] = rooms[i][j] + 1
                    doors.append((x, y))
        
    # TC: O(m*n)
    
    # SC: O(m*n)
    
    # ref: https://leetcode.com/problems/walls-and-gates/discuss/72753/6-lines-O(mn)-Python-BFS
    # ref: https://leetcode.com/problems/walls-and-gates/discuss/72748/Benchmarks-of-DFS-and-BFS
        
