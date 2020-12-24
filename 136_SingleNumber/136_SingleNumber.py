class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        HashTable
        '''
        d = collections.Counter(nums)
        for k in d:
            if d[k] == 1:
                return k
            
    # TC: O(n)
    
    # SC: O(n)
