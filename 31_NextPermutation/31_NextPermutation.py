class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        lexicographical order:
        before: 1,3,123,132,1215,143,21
        after: 1,1215,123,132,143,21,3 
        """
        i = len(nums)-2
        while i >= 0 and nums[i+1] <= nums[i]:
            # if nums[i+1] <= nums[i]: # you cant have this if statement for judging nums[i+1] and nums[i]. 
                                       # As if this statement does not meet, and i-= 1 is under if
                                       # this will be an infinite while loop. So is for the while loop below
            i -= 1
        
        if i >= 0:
            j = len(nums)-1
            while j >= 0 and nums[j] <= nums[i]:
                # if nums[j] <= nums[i]:
                j -= 1
            self.swap(nums, i, j)
        self.reverse(nums, i+1)
        
    def swap(self, numList, i, j):
        temp = numList[i]
        numList[i] = numList[j]
        numList[j] = temp
    
    def reverse(self, numList, start):
        i = start
        j = len(numList) - 1
        while i < j:
            self.swap(numList, i, j)
            i += 1
            j -= 1
            
    # TC: O(n)
    # In worst case, only two scans of the whole array are needed.
    
    # SC: O(1)
    # No extra space is used. In place replacements are performed.
