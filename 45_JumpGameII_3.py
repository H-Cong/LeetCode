class Solution:
    def jump(self, nums: List[int]) -> int:
        
        if len(nums) < 2: return 0                      
        
        jump = 1                                        
        curr_max = max_reach = nums[0]                  
                                                        
        for i in range(1, len(nums)):                   
            if max_reach >= len(nums) - 1:              
                return jump
            
            curr_max = max(curr_max, i + nums[i])
                        
            if i == max_reach:                       
                max_reach = curr_max  
                jump += 1                               
        
        return jump
    
    # TC: O(n)
    # n is the len(nums), as we only scan the list once
    
    # SC: O(1)
    # we only init 3 variables, thus space is constant
