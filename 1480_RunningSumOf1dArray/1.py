class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        
        for i, n in enumerate(nums):
            if i == 0:
                res[i] += n
            else: 
                res[i] += res[i-1] + n
    
        return res
    
    # TC: O(n)
    
    # SC: O(n)
