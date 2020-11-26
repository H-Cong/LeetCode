class Solution:
    def jump(self, nums: List[int]) -> int:
        lastGoodPosition = len(nums) - 1 
        count = 0
        while lastGoodPosition != 0:
            for i in range(len(nums)-1):
                if i + nums[i] >= lastGoodPosition:
                    lastGoodPosition = i
                    count += 1
                    break
        
        return count
    
    # TC: O(n^2) I think
    # in a case of [1, 1, 1, ..., 1, 1]
    # it takes n-1 steps to change lastGP from n-1 to n-2
    # n-2 steps from n-2 to n-3
    # ...
    # 1 step from 2 to 1
    # thus it is 1 + 2 + ... + n-1 = (n-1)/2*(1 + n-1) = n*(n-1)/2 ~ n^2
    
    
    # SC: O(1)
    
    # this is a TLE solution tho
            
