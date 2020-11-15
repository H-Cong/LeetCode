class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == nums[i+1]:
                return nums[i]
        
        return None
    
    # TC: O(nlogn)
    # The sort invocation costs O(nlgn) time in Python and Java, so it dominates the subsequent linear scan.
    
    # SC: O(1)
    # Here, we sort nums in place, so the memory footprint is constant. If we cannot modify the input array, 
    # then we must allocate linear space for a copy of nums and sort that instead.
