class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        '''
        iteration could word with O(n)
        binary search is better
        '''
        if not nums: return None
        n = len(nums)
        l = 0
        r = n - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] == target: # if we found target
                return True
            if nums[m] < nums[r]: # if right part is in order
                if nums[m] < target <= nums[r]: # if target is in right part
                    l = m + 1 # you have to have this + 1
                else:
                    r = m - 1
            elif nums[m] > nums[r]: # if left part is in order
                if nums[l] <= target < nums[m]: # if target is in left part
                    r = m - 1
                else:
                    l = m + 1 # you have to have this + 1
            else:
                r -= 1 # if right part is a flat line, i.e. all numbers are equal
        
        return nums[l] == target
    
    # TC: best O(logn) worst O(n)
    # Worst case: This happens when all the elements are the same 
    # and we search for some different element. At each step, we 
    # will only be able to reduce the search space by 1
    # Best case: This happens when all the elements are distinct. 
    # At each step, we will be able to divide our search space into 
    # half just like a normal binary search.
    
    # SC: O(1)

    # Since we have checked whetehr mid is the target, thus we can use
    # l = m + 1 and r = m - 1 to skip m in this case camparing to LeetCode 153
