class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        Greedy
        '''
        if len(nums) == 1: return nums[0]
        n = len(nums)
        curr_sum = max_sum = nums[0]
        for i in range(1, n):
            curr_sum = max(nums[i], curr_sum + nums[i]) # 1
            max_sum = max(max_sum, curr_sum)
        
        return max_sum
    
    # TC: O(n)
    
    # SC: O(1)
    
    # 1. curr_sum is either a single nums[i] or a consecutive sum of previous x numbers
    #    by comparing those two, we determine whether we need a fresh subarray start
