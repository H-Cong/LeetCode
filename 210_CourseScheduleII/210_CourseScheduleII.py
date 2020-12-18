class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        Topological Sort + BFS. Similar: 207
        '''
        graph = collections.defaultdict(list)
        inDegree = [0]*numCourses
        ans = []
        for p in prerequisites:
            graph[p[1]].append(p[0])
            inDegree[p[0]] += 1
        
        queue = deque()
        for i in range(len(inDegree)):
            if inDegree[i] == 0:
                queue.append(i)
        
        while queue:
            curr = queue.popleft()
            canTake = graph[curr]
            if canTake:
                for i in canTake:
                    inDegree[i] -= 1
                    if inDegree[i] == 0:
                        queue.append(i)
            ans.append(curr)
        
        if max(inDegree) != 0:
            return []
        
        return ans
    
    # TC: O(n)
    
    # SC: O(n)
    
    # ref: My LeetCode 207 solution 2
