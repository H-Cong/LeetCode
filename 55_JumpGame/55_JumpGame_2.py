class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        Greedy
        '''
        lastGoodIndex = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= lastGoodIndex:
                lastGoodIndex = i
        
        return lastGoodIndex == 0
    
    # TC: O(n)
    
    # SC: O(1)
