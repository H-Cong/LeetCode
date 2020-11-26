class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
            else:
                return nums[i]
        
        return None
    
    # TC: O(n)
    # Set in both Python and Java rely on underlying hash tables, so insertion and lookup have
    # amortized constant time complexities. The algorithm is therefore linear, as it consists 
    # of a for loop that performs constant work n times.
    
    # SC: O(n)
    # In the worst case, the duplicate element appears twice, with one of its appearances 
    # at array index n-1. In this case, seen will contain n−1 distinct values, and will therefore
    # occupy O(n) space.    
