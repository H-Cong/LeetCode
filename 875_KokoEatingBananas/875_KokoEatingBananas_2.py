import math
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        # Binary Search
        '''
        Binary search
        有两个整数A和B，A>1,B>1，UP（A/B）表示向上取整。
        求证 UP(A/B)=(A+B-1)//B。
        '''
        l = 1
        r = max(piles)
        while l < r:
            m = l + (r - l) // 2
            time = 0
            for pile in piles:
                # time += (pile + m - 1) // m
                time += math.ceil(pile/m)
            if time > H:
                l = m + 1
            else:
                r = m
        return l
    
    # TC: O(nlog(max(piles))
    # for loop takes O(n), binary search between (1, max(piles)) takes O(log(max(piles)))
    
    # SC: O(1)
    
    # NOTE: to caculate time, we cant sum all pile then divid by m
    # e.g. time = math.ceil(sum(piles) / m) as for all pile < K, Koko is not allowed to continue
    # eating after finishing that pile, we have to calcute the time for each pile first
