class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            if n < 0:
                continue
            else:
                while n <= len(nums) and n > 0:
                    tmp = nums[n-1]
                    nums[n-1] = float('inf')
                    n = tmp
                    print(nums)
        for i in range(len(nums)):
            if nums[i] != float('inf'):
                return i+1
            
        return len(nums)+1
        
        # TC: I think O(n) 
        # Two for loop with o(n) 
        
        # SC: O(1)
        # No extra space is needed
        
        """
        Idea: change nums[n-1] to float('inf') for all n in nums if 1 <= n <= len(nums), 
        meaning that we have seen n in nums. Then we traverse nums once more, and find 
        the first idx such that nums[idx] != float('inf'), then idx+1 will be the first 
        missing positive in nums. If no such idx exists, it means that we have seen 
        1, 2, ..., len(nums) in nums, hence the first missing positive is len(nums)+1.

        ref: https://leetcode.com/problems/first-missing-positive/discuss/231337/Python-solution
        """
