class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        DP
        '''
        if len(nums) == 1: return nums[0]
        
        prevMax1, prevMax2, currMax1, currMax2 = 0, 0, 0, 0
        
        for i, n in enumerate(nums):
            if 0 <= i < len(nums) - 1:
                temp = currMax1
                currMax1 = max(prevMax1 + n, currMax1)
                prevMax1 = temp
            if 1 <= i < len(nums):
                temp = currMax2
                currMax2 = max(prevMax2 + n, currMax2)
                prevMax2 = temp
            
        return max(currMax1, currMax2)
        
        
    # TC: O(n)
    
    # SC: O(1)
    
    # HINT: comparing to House Robber I, "the problem becomes to rob either House[1]-House[n-1] 
    # or House[2]-House[n], depending on which choice offers more money.
    # BUT NOW YOU NEED TO TAKE CARE OF THE CORNER CASE AS i IS CHECKED WITHIN FOR LOOP
    
    # ref: https://leetcode.com/problems/house-robber-ii/solution/
