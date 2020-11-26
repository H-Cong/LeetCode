# Two pointers
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # set diff to be a very large number
        diff = float('inf')
        nums.sort()
        for i in range(len(nums)):
            lo, hi = i+1, len(nums)-1
            while(lo < hi):
                sum = nums[i] + nums[lo] + nums[hi]
                if abs(target - sum) < abs(diff):
                    diff = target - sum
                if sum < target:
                    lo += 1
                else:
                    hi -= 1
                    
            if diff == 0:
                break
        return target - diff
    
    # TC: O(n^2 + nlogn) = O(N^2)
    # sort() takes O(nlogn)
    # Inner loop will do binary search n times
    # Outer loop will loop n times
    
    # SC:O(n)
    # .sort() in python takes O(n)
