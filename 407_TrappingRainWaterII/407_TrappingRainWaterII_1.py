import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        '''
        heap + BFS
        '''
        
        if not heightMap or len(heightMap) < 3 or len(heightMap[0]) < 3: 
            return 0
        
        row = len(heightMap)
        col = len(heightMap[0])
        heap = []
        visited = [[False] * col for _ in range(row)] # dont put row first!!!!!!!
        ans = 0
        
        # put all boarder heights into heap
        for i in range(row):
            for j in range(col):
                if i == 0 or i == row - 1 or j == 0 or j == col - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True
        
        while heap:
            height, x, y = heapq.heappop(heap) # this will pop the smallest heap item
            for i, j in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if 0 <= i < row and 0 <= j < col and not visited[i][j]:
                    ans += max(0, (height - heightMap[i][j]))
                    heapq.heappush(heap, (max(height, heightMap[i][j]), i, j))
                    visited[i][j] = True
        
        return ans
    
    # TC: O(row*col*2log(row+col))
    # this comes mainly when building the heap O(n * n * logn) as heapq.heappush() has worst O(logn) time
    # ppl in the discussion say it is a O(m*n*log(m*n)). I cant prove why the length of heap can reach to m*n

    # SC: O(row+col)
    # I think heap takes row+col complexity
