class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        DP
        '''
        dp = [1] * len(nums)
       
        for i in range(1, len(nums)):
            for j in range(i): # bc curr LIS till ith position has nothing to do with elements after ith
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1) # dp[i] depends on the LIS before i
        
        return max(dp)
    
    # TC: O(n^2)
    
    # SC: O(n)
    
    
