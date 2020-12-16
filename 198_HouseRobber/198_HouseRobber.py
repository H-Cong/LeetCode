class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        DP
        '''
        prevMax, currMax = 0, 0
        for n in nums:
            temp = currMax
            currMax = max(prevMax + n, currMax)
            prevMax = temp
        
        return currMax
    
    # TC: O(n)
    
    # SC: O(1)
    
    # prevMax: if curr n is in ith position, then prevMax is the rob max till i-2th position
    # currMax: similary, currMax will be the rob max till i-th position
    
    # ref: https://leetcode.com/problems/house-robber/solution/
