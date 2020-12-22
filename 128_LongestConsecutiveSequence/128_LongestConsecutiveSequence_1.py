class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        Sort
        '''
        if not nums:
            return 0

        nums.sort()

        longest_streak = 1
        current_streak = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1]+1:
                    current_streak += 1
                else:
                    longest_streak = max(longest_streak, current_streak)
                    current_streak = 1

        return max(longest_streak, current_streak)
    
    # TC: O(nlogn)
    
    # SC: O(1) or O(n)
    # For the implementations provided here, the space complexity is constant 
    # because we sort the input array in place. If we are not allowed to modify 
    # the input array, we must spend linear space to store a sorted copy.


