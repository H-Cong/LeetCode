class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        '''
        Two Pointer
        '''
        sum_, left = 0, 0
        ans = len(nums) + 1
        for right, n in enumerate(nums):
            sum_ += n
            while sum_ >= s:
                ans = min(ans, right - left + 1)
                sum_ -= nums[left]
                left += 1
        
        return ans if ans <= len(nums) else 0
    
    # TC: O(n)
    
    # SC: O(1)
