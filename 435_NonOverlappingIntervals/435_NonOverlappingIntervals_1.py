class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        Greedy. Sort by start.
        '''
        if not intervals or len(intervals) == 1: return 0
        intervals.sort()
        ans = 0
        currEnd = intervals[0][1]
        for i,x in enumerate(intervals):
            if i == 0: continue
            if x[0] < currEnd:
                currEnd = min(x[1], currEnd)
                ans += 1
            else:
                currEnd = x[1]
        
        return ans
    
    # TC: O(nlogn)
    
    # SC: O(1)
    
    # ref: https://leetcode.com/problems/non-overlapping-intervals/discuss/91768/Python-greedy-solution-with-explanation
