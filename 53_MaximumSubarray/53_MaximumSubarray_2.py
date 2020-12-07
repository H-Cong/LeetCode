class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        DP
        '''
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1] # 1
        
        return max(nums)
    
    # TC: O(n)
    
    # SC: O(1)
    
    # 1. this modifies the list and use num[i] to be a new start or to store
    #    the previous subarry which has the max_sum so far
