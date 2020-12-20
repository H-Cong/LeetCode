class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
        HashTable
        '''
        hashmap = {}
        for index,value in enumerate(nums): 
            if hashmap.get(value, -1) >= 0: # -1 will be returned if a value key does not exist
                diff = index - hashmap[value] 
                if diff <= k:
                    return True
            hashmap[value] = index
        return False
    
    # TC: O(n)
    
    # SC: O(n)
