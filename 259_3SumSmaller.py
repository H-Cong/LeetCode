class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        ans = 0
        nums.sort()
        """
        A more precise way to define range of for loop is range(len(nums)-2)
        This will make sure lo is always smaller than hi when initialized at
        the beginning of each for loop. However, using range(len(nums)) also
        works as hi is len(nums)-1 and while loop is always checking lo<hi
        """
        for i in range(len(nums)):
            lo, hi = i+1, len(nums)-1
            while(lo < hi):
                sum = nums[i] + nums[lo] + nums[hi]
                if sum < target:
                    # hi - lo means when lo IS FIXED, how many hi indices fit the creteria 
                    ans += hi - lo
                    lo += 1
                else:
                    hi -= 1
                
        return ans
    
    # TC: O(n^2)
    # both lo and hi traverse at most n steps
    
    # SC: O(n)
    # Sort in Python take O(n) space in worst case.
