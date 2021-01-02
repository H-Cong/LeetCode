class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        '''
        DFS
        '''
        res = 0
        n = len(isConnected)
        visited = set()
        for i in range(n):
            if i not in visited:
                res += 1
                self.dfs(i, visited, isConnected)
        
        return res
        
    def dfs(self, i, visited, isConnected):
        visited.add(i)
        n = len(isConnected)
        for j in range(n):
            if isConnected[i][j] and j not in visited:
                self.dfs(j, visited, isConnected)
                
    # TC: O(n^2) where n is number of nodes in the graph
    
    # SC: O(n) for the visited
    
    # ref: https://leetcode.com/problems/number-of-provinces/discuss/101464/python-dfs-iter-version
    # ref: https://leetcode.com/problems/number-of-provinces/discuss/101431/Stupid-question%3A-How-is-this-question-different-from-Number-of-Islands
