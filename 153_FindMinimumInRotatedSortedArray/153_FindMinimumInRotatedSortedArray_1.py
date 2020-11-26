class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        iteration
        '''
        n = len(nums)
        if n == 1 or nums[0] < nums[-1]:
            return nums[0]
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                return nums[i]
        
        return -1
    
    # TC: O(n)
    
    # SC: O(1)
