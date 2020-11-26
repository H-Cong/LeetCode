class Solution:
    def jump(self, nums: List[int]) -> int:
        
        if len(nums) < 2: return 0                      # corner case
        
        jump = 1                                        # if not corner case, at least 1 jump is needed
        curr_max = max_reach = nums[0]                  # max_reach to record the max index can be reached with current # of jump
                                                        # curr_max to record the max index can be reached from the current index
        
        
        for i in range(1, len(nums)):                   # we start from index 1 if not corner case, but including 0 still works
            if max_reach >= len(nums) - 1:              # termination check
                return jump
            if i < max_reach:                           # if i is within the reach of current jump
                if i + nums[i] > curr_max:              # we update the current max reach if a larger one exists
                    curr_max = i + nums[i]              
                    if curr_max >= len(nums) - 1:       # early terminatin check, but solution still works even without this
                        return jump + 1                 # remember to add 1 to current jump if you use early termination
                                                        # here we dont jump yet until we figure out the max range we can reach 
                                                        # if we jump one more time
                        
            else:                                       # when we enter this else statement, it means max_reach is not the end of list
                                                        # thus we have to jump now
                max_reach = max(curr_max, i + nums[i])  # we update our max_reach using the curr_max recorded so far or i + nums[i]
                jump += 1                               # and we add 1 to jump to add this jump
        
        return jump
    
    # TC: O(n)
    # n is the len(nums), as we only scan the list once
    
    # SC: O(1)
    # we only init 3 variables, thus space is constant
