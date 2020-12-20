class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
        HashTable
        '''
        s = set(nums)
        if len(s) == len(nums): return False
        
        d = collections.defaultdict(list)
        for i, n in enumerate(nums):
            d[n].append(i)
        
        for value in d.values():
            if len(value) > 1:
                for i in range(len(value)-1):
                    if value[i+1] - value[i] <= k:
                        return True
        return False
    
    # TC: O(n)
    # d.values() contains all index, we loop all index only once.
    
    # SC: O(n)
