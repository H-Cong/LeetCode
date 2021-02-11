class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        d1 = collections.Counter(nums1)
        d2 = collections.Counter(nums2)
        res = []
        for k1 in d1.keys():
            if k1 in d2.keys():
                res += [k1] * min(d1[k1], d2[k1])
        
        return res
    
    # TC: O(n+m)
    
    # SC: O(min(m,n))
