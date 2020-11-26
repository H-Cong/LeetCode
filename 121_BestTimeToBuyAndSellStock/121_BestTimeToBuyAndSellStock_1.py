# This solution yields TLE error
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        prof = 0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                if prices[i] < prices[j]:
                    curr_prof = prices[j] - prices[i]
                    prof = max(prof, curr_prof)
        
        return prof
    
    # TC: O(n^2)
    
    # SC: O(1)
