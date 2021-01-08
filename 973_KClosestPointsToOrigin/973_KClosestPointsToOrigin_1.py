class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        res = []
        for l in points:
            r = l[0]**2 + l[1]**2
            res.append([l,r])
        
        res.sort(key = lambda x:x[1])
        columns = list(zip(*res)) # transpose rows to columns
        
        return columns[0][:K]
    
    # TC: O(nlogn)
    
    # SC: O(n)
    
    # ref: https://stackoverflow.com/questions/30062429/how-to-get-every-first-element-in-2-dimensional-list/30062458#30062458
