class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        Greedy. Sort by end.
        '''
        if not intervals or len(intervals) == 1: return 0
        intervals.sort(key=lambda x:x[1])
        cnt = 1
        curr = intervals[0]
        
        for x in intervals:
            if curr[1] <= x[0]:
                cnt += 1
                curr = x
            
        return len(intervals) - cnt
    
    # TC: O(nlogn)
    
    # SC: O(1)
    
    # ref: https://leetcode.com/problems/non-overlapping-intervals/discuss/793070/Python-O(n-log-n)-sort-ends-with-proof-explained
