class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        Hashmap
        '''
        d = collections.Counter(nums)
        
        return d.most_common(1)[0][0]
    
    # TC: O(n)
    
    # SC: O(n)
    
    # ref: https://stackoverflow.com/questions/20950650/how-to-sort-counter-by-value-python
    
