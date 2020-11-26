class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        
        # make sure len1 is always the shorter length
        if len1 > len2:
            return self.findMedianSortedArrays(nums2, nums1)
        
        total_len = len1 + len2
        
        # use l and r to maintain the range of binary search
        l, r = 0, len1
        
        # THIS HAS TO BE <= NOT <
        while l <= r: 
            # calculate # of numbers on the left of cut point of nums1
            l_nums_1 = (l + r) // 2  # or you can use l + (r - l) // 2 to avoid potential overflow
            
            # calculate # of numbers on the left of cut point of nums2
            l_nums_2 = (total_len + 1) // 2 - l_nums_1
            
            L1 = float('-inf') if l_nums_1 == 0 else nums1[l_nums_1-1]
            L2 = float('-inf') if l_nums_2 == 0 else nums2[l_nums_2-1]
            R1 = float('inf') if l_nums_1 == len1 else nums1[l_nums_1]
            R2 = float('inf') if l_nums_2 == len2 else nums2[l_nums_2]
            
            # adjust the binary search range if (L1 <= R2 && L2 <= R1) is not met 
            if L1 > R2:
                r = l_nums_1 - 1
            elif L2 > R1:
                l = l_nums_1 + 1
            else:
                if total_len % 2 == 0:
                    return (max(L1, L2)+min(R1, R2)) / 2
                else:
                    return max(L1, L2)
                
        return -1
    
    # TC: O(log(min(m,n)))
    # At first, the searching range is [0,m]. And the length of this searching range will be reduced
    # by half after each loop. So, we only need log(m) loops. Since we do constant operations in each 
    # loop, so the time complexity is O(log(m)). Since m ≤ n, so the time complexity is O(log(min(m,n))).
    
    # SC: O(1)
    # We only need constant memory to store local variables, so the space complexity is O(1).
            
        
