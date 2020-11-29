class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        '''
        Brute Force
        '''
        if not nums or len(nums) < 2: return 0
        
        n = len(nums)
        
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] > 2*nums[j]:
                    ans += 1
        
        return ans
    
    # TC: O(n^2)
    
    # SC: O(1)

    # TLE
