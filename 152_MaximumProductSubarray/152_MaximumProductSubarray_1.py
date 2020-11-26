class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return None
        ans = nums[0]
        for i in range(len(nums)):
            curr = 1
            for j in range(i, len(nums)):
                curr *= nums[j]           # since j also starts from 0
                ans = max(curr, ans)
            
        return ans
    
    # TC: O(n^2)
    
    # SC: O(1)
    
    # This brute force solution will yield a TLE error
