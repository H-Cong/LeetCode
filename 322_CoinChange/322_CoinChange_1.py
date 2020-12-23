class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        DP TopDown. Similar: Stone jump? Jump game?
        '''
        if amount < 1: return 0
        d = {}
        self.helper(amount, coins, d)
        return d[amount] if d[amount] != float('inf') else -1
    
    def helper(self, amount, coins, d):
        if amount == 0: return 0
        if amount < 0: return float('inf')
        if amount in d: return d[amount]
        
        min_way = float('inf')
        for c in coins:
            min_way = min(min_way, self.helper(amount-c, coins, d)+1)
        
        d[amount] = min_way
        
        return min_way
    
    # TC: O(a*c) where a is the amount and c is the number of coins
    # In the worst case the recursive tree of the algorithm has height 
    # of a and the algorithm solves only a subproblems because it caches 
    # precalculated solutions in a table. Each subproblem is computed with 
    # c iterations, one by coin denomination. Therefore there is O(a*c) time complexity.
    
    # SC: O(a)
    # space taken by dic as well as the recursion
    
    # NOTE: that when amount is 0, there is one way to make that amount by
    # providing 0 coins
