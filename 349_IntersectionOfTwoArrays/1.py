class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2): return self.intersection(nums2, nums1)
        n2 = set(nums2)
        n1 = set(nums1)
        res = []
        for n in n2:
            if n in n1:
                res.append(n)
        
        return res
    
    # TC: O(n+m)
    
    # SC: O(n+m)
    
    
