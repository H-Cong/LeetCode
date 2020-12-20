class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        Hashset
        '''
        n = set(nums)

        return len(n) != len(nums)

    # TC: O(n)

    # SC: O(n)
