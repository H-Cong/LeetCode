class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) <= 1 or numbers[0] > target: return None
        l, r = 0, len(numbers)-1
        
        while l < r:
            aim = target - numbers[l]
            if numbers[r] > aim:
                r -= 1
            elif numbers[r] < aim:
                l += 1
            else:
                return [l+1, r+1]
        
        return None
    
    # TC: O(n)
    
    # SC: O(1)
        
