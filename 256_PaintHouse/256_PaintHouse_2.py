class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        '''
        DP
        '''
        if len(costs) == 0: return 0
        prev_row = costs[-1]
        for i in reversed(range(len(costs)-1)):
            curr_row = copy.deepcopy(costs[i])
            curr_row[0] += min(prev_row[1], prev_row[2])
            curr_row[1] += min(prev_row[0], prev_row[2])
            curr_row[2] += min(prev_row[0], prev_row[1])
            prev_row = curr_row
        
        return min(prev_row)
    
    # TC: O(n)
    
    # SC: O(1)
    
    # ref: https://leetcode.com/problems/paint-house/solution/
    # GREAT ARTICLE
