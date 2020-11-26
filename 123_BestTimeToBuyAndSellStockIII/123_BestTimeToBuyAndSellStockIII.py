class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        t1_cost, t2_cost = float('inf'), float('inf')
        t1_prof, t2_prof = 0, 0
        
        for price in prices:
            t1_cost = min(t1_cost, price)
            t1_prof = max(t1_prof, price - t1_cost)
            
            t2_cost = min(t2_cost, price - t1_prof)
            t2_prof = max(t2_prof, price - t2_cost)
            
        return t2_prof
    
    # TC: O(n)
    # min() and max() generally have O(N) TC. But in this case its O(2) so we ignore them
    
    # SC: O(1)
    
    """
    Its tricky to understand t2_cost. But basically, if t2_cost is negative, it means that
    you are still making money even after you make the 2nd purchase of the stock. 
    E.g. say in t1, you buy stock at price 1 and hold them till price 4, you are currently 
    making profit of 3. Then the next price is 2, and you make the 2nd purchase. t2_cost 
    will be -1. This means you are still holding profit of 1 even after the 2nd purchase.
    If you sell stock at this price 2 moment, it will give t2_prof back to 3 again, which 
    means t2_prof is still 3 at this point. 
    """
    
    """
    IDEA:
    t1 min cost = min(t1 min cost, curr price)
    t1 max profit = max(t1 max profit, curr price - t1 min cost)
    
    we then reinvest t1 max profit to t2, thus
    t2 cost = curr price - t1 max profit
    thus
    t2 min cost = min(t2 min cost, curr price - t1 max profit)
    similar to how t1 max profit is calculated, we then have
    t2 max profit = max(t2 max profit, curr price - t2 min cost)
    
    finally we return t2 max profit
    
    SAME IDEA can be applied to a more general most N transaction stock buy-sell problem
    """
