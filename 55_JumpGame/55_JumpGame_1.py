class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        self.ans = False
        for n in range(1, nums[0]+1):
            if n == len(nums) - 1:
                return True
        
            self.step(n, n, nums)
        
        return self.ans
    
    
    def step(self, n, index, nums):
        
        for i in range(1, nums[index]+1):
            if n + i == len(nums) - 1:
                 self.ans = True
            else:
                curr_n = n + i
                if index+i < len(nums): self.step(curr_n, index+i, nums)
        
    
    # TC: O(n^n) ??
    # where n is the sum of all number in nums?? 
    
    # SC： O(1)
    
    # rises a TLE error. but can pass simple tasks. I guess it works, just too slow.
    # took me half day to come up with this. somewhat glad even tho its a TLE.
