class Solution:
    def jump(self, nums: List[int]) -> int:
        
        if len(nums) <= 1: return 0
        
        l, r = 0, nums[0]
        times = 1
        
        while r < len(nums) - 1:
            times += 1
            nxt = max(i + nums[i] for i in range(l, r + 1))
            l, r = r + 1, nxt
        
        return times
    
    # TC: O(n)
    # n is the len(nums), as we only scan the list once
    
    # SC: O(1)
    # we only init 3 variables, thus space is constant
