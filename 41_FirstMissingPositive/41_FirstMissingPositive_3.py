class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        INF = n + 1
    
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = INF # marks zero or negative numbers as infinitive positive numbers
                
        for i in range(n):
            x = abs(nums[i]) - 1 # use index start with zero
            if x < n:
                nums[x] = -abs(nums[x]) # mark `x` as visited by marking `nums[x]` as negative
                    
        for i in range(n):
            if nums[i] > 0: # if nums[i] is positive -> number (i+1) is not visited.
                return i + 1
        return n + 1
        
        # TC: I think O(n) 
        # Two for loop with o(n) 
        
        # SC: O(1)
        # No extra space is needed
        
        """
        Idea:

        1. Marks zero or negative numbers as positive numbers.
        2. Mark number x as visited by marking nums[x] as negative, by using (x-1) we can use 
           index 0 of nums array.
        3. Interate from 0..n-1, if nums[i] > 0 then it means the number i+1 is the smallest 
           positive number which is missing.
           
        ref: https://leetcode.com/problems/first-missing-positive/discuss/872224/JavaPython-Supper-Clean-and-Concise-Time-O(N)-Space-O(1)

        """
