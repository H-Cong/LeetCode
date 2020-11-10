class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return None
        curr_max = nums[0]
        curr_min = nums[0]
        ans = curr_max
        
        for i in range(1, len(nums)):
            temp_max = max(nums[i], nums[i]*curr_max, nums[i]*curr_min)
            curr_min = min(nums[i], nums[i]*curr_max, nums[i]*curr_min)
            
            curr_max = temp_max # you have to use a temp max here because curr_min 
                                # is calculated based on curr_max, you dont want it
                                # to be changed before curr_min is calculated
            
            ans = max(ans, curr_max)
        
        return ans
    
    # TC: O(n)
    # where n is the size of nums. The algorithm achieves linear runtime since we are going through nums only once
    
    # SC: O(1)
    # since no additional space is consumed rather than variables which keep track of the maximum product so far, 
    # the minimum product so far, current variable, temp variable, and placeholder variable for the result.
    
    # ref: https://leetcode.com/problems/maximum-product-subarray/solution/
    
