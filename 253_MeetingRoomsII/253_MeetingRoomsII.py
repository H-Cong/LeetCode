class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        '''
        Priority Queue. Min Heap.
        '''
        if not intervals: return 0
        room = []
        intervals.sort()
        heapq.heappush(room, intervals[0][1])
        
        for i in intervals[1:]:
            if i[0] >= room[0]:
                heapq.heappop(room)
            heapq.heappush(room, i[1])
            
        
        return len(room)
    
    # TC: O(nlogn)
    # sorting takes O(nlogn)
    # we have the min-heap. In the worst case, all n meetings will collide with each other. 
    # In any case we have n add operations on the heap. In the worst case we will have n 
    # extract-min operations as well. Overall complexity being O(nlogn) since extract-min 
    # operation on a heap takes O(logn).
    
    # SC: O(n)
