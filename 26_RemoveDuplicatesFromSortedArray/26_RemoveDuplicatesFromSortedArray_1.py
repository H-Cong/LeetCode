class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # for i in range(len(nums)):
        #     n = len(nums)
        #     if i != len(nums) - 1:
        #         if nums[i] == nums[i+1]:
        #             nums.remove(nums[i+1])
        
        '''
        The way above does not work. Though nums gets shorter after each duplicate spotted
        The range of for loop still remain the same, although n does change after each .remove()
        Weird...
        '''
        for i in range(len(nums)):
            while i < len(nums) - 1: # while loop to deal with > 2 duplicates of one number
                if nums[i] == nums[i+1]:
                    nums.remove(nums[i+1])
                else:
                    break
        
        return len(nums)
    
    # TC: O(n^2)
    
    # SC: O(1)
