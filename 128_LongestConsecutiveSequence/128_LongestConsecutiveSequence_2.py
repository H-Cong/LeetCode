class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        Hashset
        '''
        if not nums:
            return 0

        s = set(nums)
        ans = 0
        
        for n in s:
            if n-1 not in s:
                curr = n
                currLen = 1
                while curr + 1 in s:
                    curr += 1
                    currLen += 1
                ans = max(ans, currLen)

        return ans
    
    # TC: O(n)
    
    # SC: O(n)
    

