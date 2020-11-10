class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        
        # if not nums or nums[0] > target: # this statement only holds when target is > 0
        if not nums:
            return res
        
        for i in range(len(nums)-3): # you can set this range to len(nums)-3 or just len(nums)
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            threeRes = self.threeSum(nums[i+1:], target-nums[i])
            if threeRes:
                for _res in threeRes:
                    res.append([nums[i]]+_res)
            
        return res
    
    def threeSum(self, nums, target):
        res = []
        # nums.sort() # no need to sort again
        
        # if nums[0] > target: # this statement only holds when target is > 0
        #     return res
        
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
                
            l, r = i+1, len(nums)-1
            while l < r: # this statement block the possibility of l exceed the index
                _sum = nums[i] + nums[l] + nums[r]
                
                if _sum < target:
                    l += 1
                elif _sum > target:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
            
        return res
    
    # TC: O(n^3)
    # O(n) in fourSum, O(n) in threeSum for loop, O(n) in threeSum while loop
    
    # SC: O(n)?
    # for the sorting function?
    
            
            
            
            
