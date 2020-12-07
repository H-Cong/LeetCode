class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in reversed(range(len(nums))):
            if nums[i] == 0:
                for j in range (i, len(nums)-1):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        
    # TC: O(n^2)
    
    # SC: O(1)
