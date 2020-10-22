class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        # sort cant be used here as it will change the index of the ans
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    ans.append(i)
                    ans.append(j)
                    return ans
        return ans
    
    # TC: O(n^2)
    # O(n) for each for loop
    
    # SC: O(1)
