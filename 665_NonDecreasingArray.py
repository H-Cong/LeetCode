class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        peak = 0
        low = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                peak += 1
                if i == 0:
                    continue
                else:
                    if nums[i-1] <= nums[i+1]:
                        continue
                    elif i <= len(nums)-3 and nums[i] > nums[i+2]:
                        return False
                    else:
                        continue
                    
        return peak <= 1 
    
    # TC: O(n)
    
    # SC: O(1)
    
    # Took me some time to figure out all situations
    # In general one needs to figure out when nums[i] > nums[i+1], 
    # is nums[i] a pure peak e.g. 1,2,6,3,4
    # or nums[i+1] a pure valley e.g. 6,7,1,8,9
