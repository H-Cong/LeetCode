class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        s = set()
        ans = []
        for n in nums:
            if n not in s:
                s.add(n)
            else:
                ans.append(n)
        return ans
    
    # TC: O(n)
    
    # SC: O(n)
    
