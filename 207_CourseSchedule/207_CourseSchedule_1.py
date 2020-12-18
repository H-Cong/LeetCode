class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        Topological Sorting + DFS
        '''
        graph = collections.defaultdict(list)
        for p in prerequisites:
            graph[p[0]].append(p[1])  # p[1].append(p[1]) also works
        # 0: unknown; 1: visiting; 2: visited
        states = [0] * numCourses
        
        for i in range(numCourses):
            if self.dfs(i, states, graph):
                return False
        
        return True
    
    def dfs(self, curr, states, graph): # return True if a cycle is found, False if not
        if states[curr] == 1: return True
        if states[curr] == 2: return False
        
        states[curr] = 1
        
        for course in graph[curr]:
            if self.dfs(course, states, graph):
                return True
        
        states[curr] = 2
        
        return False
    
    # TC: O(n)
    
    # SC: O(n)
    
    # IDEA: if you start from a node, then enter dfs, then
    # find a another node has a visiting state. It means there
    # must exist a cycle

    # ref:  http://zxi.mytechroad.com/blog/graph/leetcode-207-course-schedule/
