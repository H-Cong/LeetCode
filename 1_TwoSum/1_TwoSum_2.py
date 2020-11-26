class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _dict = {}
        # sort cant be used here as it will change the index of the ans
        # use hashmap to store the number and index
        for i in range(len(nums)):
            _dict[nums[i]] = i
            
        for i in range(len(nums)):
            x = target - nums[i]
            # dont forget to check the x is not the same position as the current i
            if x in _dict and _dict[x] != i:
                return[i, _dict[x]]
        return []
    
    # TC: O(n)
    # O(n) for for loop
    
    # SC: O(n)
    # for dict
