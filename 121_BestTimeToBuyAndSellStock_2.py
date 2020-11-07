class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        low_price = float('inf')
        prof = 0
        for i in range(len(prices)):
            if prices[i] < low_price:
                low_price = prices[i]
            elif prices[i] - low_price > prof:
                prof = prices[i] - low_price
        
        return prof
    
    # TC: O(n)
    
    # SC: O(1)
                    
