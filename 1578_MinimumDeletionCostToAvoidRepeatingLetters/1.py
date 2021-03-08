class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        ans = max_cost = 0
        for i in range(len(s)):
            if i > 0 and s[i] != s[i-1]:
                max_cost = 0
            ans += min(cost[i], max_cost)
            max_cost = max(cost[i], max_cost)
        
        return ans
    
    # TC: O(n)
    
    # SC: O(1)
