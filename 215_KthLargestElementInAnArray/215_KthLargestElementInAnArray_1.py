class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]
    
    # TC: O(nlogn)
    
    # SC: O(1)
    # python timsort has best O(1) SC and worst O(n) SC
