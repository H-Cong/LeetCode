class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        Hashmap
        '''
        d = collections.Counter(nums)
        
        return sorted(d, key = d.get, reverse = True)[0]
    
    # TC: O(n)
    
    # SC: O(n)
    
