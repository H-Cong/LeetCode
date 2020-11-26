# Binary Search
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                complement = target - nums[i] - nums[j]
                """
                bisect_right return the index where insert the complement number 
                while still mainteining the order of the list
                _right means if complement already exists in list, the insertion
                will be to the right of the existing value
                """
                hi = bisect_right(nums, complement, j + 1)
                lo = hi - 1
                """
                hi can be equal to len(nums). In that case, we dont need to check
                that position as the value does not exist at that position
                and it will throw a index error
                """
                if hi < len(nums) and abs(complement - nums[hi]) < abs(diff):
                    diff = complement - nums[hi]
                """
                As hi can be equal to j+1, lo can be equal to j
                if lo = j, then diff will be target - nums[i] - 2*nums[j]
                this does not fit what we need
                """
                if lo > j and abs(complement - nums[lo]) < abs(diff):
                    diff = complement - nums[lo]
            if diff == 0:
                break
        return target - diff
    
    # TC: O(n^2logn)
    # Binary search (bisect) takes O(logn)
    # Inner for loop will do binary search n times
    # Outer loop will loop n times
    
    # SC:O(n)
    # .sort() in python takes O(n)
