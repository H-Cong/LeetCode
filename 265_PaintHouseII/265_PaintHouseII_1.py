class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        '''
        DP
        '''
        if len(costs) == 0: return 0
        prev_row = costs[-1]
        
        for n in reversed(range(len(costs)-1)):
            curr_row = copy.deepcopy(costs[n])
            for c in range(len(costs[0])):
                curr_row[c] += min(prev_row[0:c] + prev_row[c+1:])
            prev_row = curr_row
        
        return min(prev_row)
    
    # TC: O(nk^2)
    # k is # of colors, min() also takes O(k)
    
    # SC: O(1)
    
    # same idea of PaintHouse 1
        
