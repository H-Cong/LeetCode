class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 1
        
        elif len(nums) == 1:
            if nums[0] == 1:
                return nums[0] + 1  
            else:
                return 1
        else:

            l = len(nums)
            for i in range(1,l+2):
                if i not in nums:
                    return i
                else:
                    None
        
        # TC: I think O(n^2) 
        # As for loop has o(n) and if i not in List takes O(n) as well
        
        # SC: O(1)
        # No extra space is needed
