class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        dp, sumA = {0}, sum(stones)
        for a in stones:
            dp = {a + x for x in dp} | {a - x for x in dp}
        return min(abs(x) for x in dp)
    
    # TC: O(ns)

    # SC: O(s)
    
    # s is the sum of stones
    # ref: https://leetcode.com/problems/last-stone-weight-ii/discuss/296350/

