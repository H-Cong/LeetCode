class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        DP
        '''
        sold, held, reset = float('-inf'), float('-inf'), 0
        for p in prices:
            pre_sold = sold
            sold = held + p
            held = max(held, reset - p)
            reset = max(reset, pre_sold)
        
        return max(sold, reset)
    
    # TC: O(n)
    
    # SC: O(1)
    
    # ref: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/solution/
