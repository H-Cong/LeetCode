class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return accumulate(nums)
        
    
    # TC: O(n)
    
    # SC: O(n)?
