class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        Gauss Formula
        '''
        n = len(nums)
        expected_sum = n*(n+1) // 2
        curr_sum = sum(nums)
        
        return expected_sum - curr_sum
            
    # TC: O(n)
    
    # SC: O(1)
