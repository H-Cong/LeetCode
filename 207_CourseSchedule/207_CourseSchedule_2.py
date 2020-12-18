class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        Topological Sorting + BFS
        '''
        graph = collections.defaultdict(list) # this graph is represented by adjacency list.
        inDegree = [0] * numCourses
        for p in prerequisites:
            graph[p[1]].append(p[0])  # In this case, we have to use p[1].append(p[0])
            inDegree[p[0]] +=1
            
        queue = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)
        
        while queue:
            curr = queue.popleft()
            canTake = graph[curr]
            if canTake:
                for i in range(len(canTake)):
                    inDegree[canTake[i]] -= 1
                    if inDegree[canTake[i]] == 0:
                        queue.append(canTake[i])
        if max(inDegree) != 0:
            return False
        
        return True
        
    # TC: O(n)
    
    # SC: O(n)
    
    # ref: https://www.youtube.com/watch?v=fskPWs3Nuhc
    
