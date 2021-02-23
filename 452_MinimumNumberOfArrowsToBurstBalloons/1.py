class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        '''
        Greedy
        '''
        if not points: return 0
        points.sort(key = lambda x : x[1])
        ans = 1
        first_end = points[0][1]
        for s, e in points:
            if first_end < s:
                ans += 1
                first_end = e
        
        return ans
    
    # TC: O(nlogn)
    
    # SC: O(n) list.sort() in Python takes O(n) space
            
