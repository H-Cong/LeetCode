class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return nums
        
        n = len(nums)
        q = k % n
        
        nums[:] = nums[n-q:] + nums[:n-q] # you cant use nums = as this wont modify the array, num[:] is a must
        
        # return nums

    # TC: O(n)
    # slicing takes O(n) time

    # SC: Im not sure whether this is a O(1) or O(n) space...
