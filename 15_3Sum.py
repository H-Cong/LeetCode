class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() # sorting has time complexity of O(nlogn)
        
        # Outer loop to tell the first value, inner loop to solve the 2sum problem
        # This is a TC of O(n^2)
        # Thus the overall TC is O(n^2)
        # The SC depends on the sorting algorithm. It can be O(1) or O(n)
        
        # First iterate the index as well as the value
        for i, v in enumerate(nums):
            
            # If the current index is not the first element but the value of it is equal
            # to the previous value, we need to continue to next element
            if i > 0 and v == nums[i - 1]: 
                continue
            
            # Left and right pointer points to the next element of current element and 
            # the last elememt of the array, respectively
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = v + nums[l] + nums[r]
                if threeSum > 0:
                    # We need to decrease the sum by shift right pointer to left by 1 index
                    r -= 1
                elif threeSum < 0:
                    # We need to increase the sum by shift left pointer to right by 1 index
                    l += 1
                else:
                    res.append([v, nums[l], nums[r]]) # Append the array to the result
                    l += 1 # Shift left pointer to right by 1 index
                    while nums[l] == nums[l - 1] and l < r:
                        # We only need to worry abou the left pointer as the right pointer 
                        # will be taken care of by the outter while loop
                        l += 1 
                
        return res                    
