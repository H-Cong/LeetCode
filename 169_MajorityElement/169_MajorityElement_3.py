class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        Boyer-Moore Voting Algorithm
        '''
        count = 0
        ans = None
        
        for n in nums:
            if count == 0:
                ans = n
            count += (1 if ans == n else -1)
            
        return ans
    
    # TC: O(n)
    
    # SC: O(1)
    
    # ref: https://leetcode.com/problems/majority-element/solution/
