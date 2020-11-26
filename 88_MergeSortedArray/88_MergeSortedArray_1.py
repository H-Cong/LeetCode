class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # set up two pointers pointing to the end of each list
        p1 = m - 1
        p2 = n - 1
        
        # set up one pointer pointing to the end of num1
        p = m + n - 1
        
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] <= nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1
        
        # insert whats left in nums2 to the front of nums1
        # p1 = -1 means all nums1 numbers have been iterated
        # p2 >= 0 means there are still numbers left in nums2
        # this if statement is actually optional
        if p1 == -1 and p2 >= 0:
            nums1[:p2+1] = nums2[:p2+1] # +1 cuz the actual index used for the list will end 1 index earlier
            
        # TC: O(n+m) = O(N)
        # SC: O(1)
        
