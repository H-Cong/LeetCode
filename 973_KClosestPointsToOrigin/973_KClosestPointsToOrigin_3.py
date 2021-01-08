class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        '''
        MaxHeap
        '''
        heap = []
        for l in points:
            dist = -(l[0]**2 + l[1]**2) # NOTE the - sign here
            if len(heap) == K:
                heapq.heappushpop(heap, (dist, l))
            else:
                heapq.heappush(heap, (dist, l))
        
        return [l for (dist, l) in heap]
            
    
    # TC: O(nlogK)
    
    # SC: O(K)
    
