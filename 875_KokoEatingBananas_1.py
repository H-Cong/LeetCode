class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        # Binary Search
        left = 1
        right = max(piles)
        
        while left < right:
            mid = left + (right-left) // 2
            if self.eatTime(piles, mid) > H:
                left = mid + 1
            else:
                right = mid
        
        return left
    
    def eatTime(self, piles, K):
        h = 0
        for pile in piles:
            if pile % K == 0:
                h += pile // K
            else:
                h += pile // K + 1
        return h
    
    # TC: O(nlog(max(piles))
    # eatTime takes O(n), binary search between (1, max(piles)) takes O(log(max(piles)))
    
    # SC: O(1)
