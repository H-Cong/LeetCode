class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        Set
        '''
        nums = set(nums)
        for n in range(len(nums) + 1):
            if n not in nums:
                return n
            
    # TC: O(n)
    
    # SC: O(n)
