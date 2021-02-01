class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        '''
        DP
        '''
        if len(costs) == 0: return 0
        prev_row = costs[0]
        n, k = len(costs), len(costs[0])
        for i in range(1, n):
            curr_row = copy.deepcopy(costs[i])
            min1 = min(prev_row)
            idx = prev_row.index(min1)
            min2 = min(prev_row[:idx]+prev_row[idx+1:])
            for j in range(k):
                if j == idx: # we cant and true min (min1) as this will lead two adjacent houses has same color
                    curr_row[j] += min2
                else:
                    curr_row[j] += min1
            prev_row = curr_row
        
        return min(prev_row)   
    
    # TC: O(nk)
    # k is # of colors
    
    # SC: O(1)
    
    # ref: https://leetcode.com/problems/paint-house-ii/solution/
    
        
