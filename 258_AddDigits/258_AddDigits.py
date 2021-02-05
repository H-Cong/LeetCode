class Solution:
    def addDigits(self, num: int) -> int:
        temp = 0
        while num > 0:
            temp += num % 10
            num //= 10
            if num == 0 and temp > 9:
                num = temp
                temp = 0
        
        return temp
    
    # TC: O(len(num))
    
    # SC: O(1)
