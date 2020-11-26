class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        print(nums)
        if len(nums) % 2 == 0:
            mid = len(nums) // 2
            return (nums[mid-1] + nums[mid]) / 2
        else:
            mid = len(nums) // 2
            return nums[mid]
        
        
        # TC: O((m+n)log(m+n))
        # .sort() dominates the TC
        
        # SC: O(m+n)
        # for nums
