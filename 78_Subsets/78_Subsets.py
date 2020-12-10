class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        Backtrack
        '''
        res = []
        for k in range(len(nums)+1):
            self.backtrack(res, 0, k, nums, [])
        
        return res

    def backtrack(self, res, first, k, nums, curr):
        if len(curr) == k:
            res.append(curr[:])
        for i in range(first, len(nums)):
            curr.append(nums[i])
            self.backtrack(res, i+1, k, nums, curr)
            curr.pop()
        
    # TC: O(n2^n)
    
    # SC: O(n2^n)
