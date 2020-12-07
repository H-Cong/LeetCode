class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastNonZeroIndex = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastNonZeroIndex], nums[i] = nums[i], nums[lastNonZeroIndex]
                lastNonZeroIndex += 1
        
    # TC: O(n)
    
    # SC: O(1)
