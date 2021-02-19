class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        m = set()
        for n in nums:
            m.add(n)
            if len(m) > 3:
                m.remove(min(m))
        if len(m) == 3:
            return min(m)
        return max(m)
    
    # TC: O(n)
    
    # SC: O(1)
