class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        # if n == 1: return nums[0]
        l = 0
        r = n-1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            elif nums[m] > nums[r]:
                l = m + 1
            else:
                r -= 1
        
        return nums[l]
    
    # TC: Best O(logn), worst O(n)
    
    # SC: O(1)

    # see also LeetCode 153
