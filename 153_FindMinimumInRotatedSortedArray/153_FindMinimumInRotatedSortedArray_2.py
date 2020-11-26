class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        binary search
        '''
        n = len(nums)
        l = 0
        r = n - 1
        
        # if nums[l] < nums[r]:
        #     return nums[l]
        
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < nums[r]: # compare mid with right is key to find out whether right part is sorted or not
                r = mid # you can not use mid - 1 here as mid could be the minimum
            else: 
                l = mid + 1
        
        return nums[l]
    
    # TC: O(logn)
    
    # SC: O(1)
