class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        if len(nums) == 0 or nums[0] > 0:
            return res
            
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
                
            l, r = i+1, len(nums)-1
            while l < r:
                _sum = nums[i] + nums[l] + nums[r]
                if _sum < 0:
                    l += 1
                elif _sum > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    # we only need to make sure left pointer is not pointing to the 
                    # same number as the previous left number
                    # the elif statement will make sure the according right number
                    # is not a duplicate as well
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res
    
    # TC: O(nlogn + n^2)
    
    # SC: O(n)
    # I think python sort takes O(n). And we ignore the space taken by the output
    
    # https://www.youtube.com/watch?v=jzZsG8n2R9A&ab_channel=NeetCode
    
