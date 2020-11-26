class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergedArray = self.mergeTwoSortedArray(nums1, nums2)
        total_len = len(mergedArray)
        if total_len % 2 == 0:
            return (mergedArray[(total_len-1)//2] + mergedArray[total_len//2]) / 2
        else:
            return mergedArray[total_len//2]
    
    def mergeTwoSortedArray(self, nums1, nums2):
        merged = [0] * (len(nums1)+len(nums2))
        i, j, k = 0, 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged[k] = nums1[i]
                k += 1
                i += 1
            else:
                merged[k] = nums2[j]
                k += 1
                j += 1
        while i < len(nums1):
            merged[k] = nums1[i]
            k += 1
            i += 1
        while j < len(nums2):
            merged[k] = nums2[j]
            k += 1
            j += 1
        
        return merged
    
    # TC: O(m+n)
    # we scan both nums1 and nums2 for once to generate merged array
    
    # SC: O(m+n)
    # this comes from the merged array
            
        
