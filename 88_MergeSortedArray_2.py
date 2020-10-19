class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # You could you the sort() function but this will increase the TC
        nums1[:] = nums1[:m] + nums2
        nums1 = nums1.sort()
        
        # or you can use the sorted() function as the following one-liner
        # nums1[:] = sorted(nums1[:m] + nums2)
        
        # Dont use nums1 = nums1[:m] + nums2
        # More info in the following link
        # https://stackoverflow.com/questions/35713891/what-is-the-meaning-of-arr-in-assignment-in-numpy
        
        # Also check out my discussion post on LeetCode
        
        # TC: O((n+m)log(n+m))
        # SC: O(1)
