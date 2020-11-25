class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        BackTracking
        '''
        return self.canJumpFromPosition(0, nums)
    
    def canJumpFromPosition(self, position, nums):
        if position == len(nums) - 1: return True
        
        furthestJump = min(position + nums[position], len(nums) - 1)
        
        for nextPosition in range(position + 1, furthestJump + 1):
            if self.canJumpFromPosition(nextPosition, nums):
                return True
        
        return False
    
    # TC: O(2^n)
    # There are 2^n (upper bound) ways of jumping from the first position to the last,
    # where nn is the length of array nums.
    
    # SC: O(n)
    # Recursion requires additional memory for the stack frames.
