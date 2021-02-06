class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0: return False
        for i in [2, 3, 5]:
            while num % i == 0:
                num /= i
        
        return num == 1
    
    # TC: O(x)
    # x is how big is num???
    
    # SC: O(1)
    
    # a == b < c means a == b and b < c
