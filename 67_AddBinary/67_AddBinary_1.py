class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        ans = ""
        while a or b or carry:
            x = int(a[-1]) if a else 0
            y = int(b[-1]) if b else 0
            _sum = x + y + carry
            carry = _sum // 2
            remainder = _sum % 2
            ans = str(remainder) + ans # be aware the order w.r.t. the + sign
            a = a[:-1]
            b = b[:-1]
        
        return ans
    
    # TC: O(n^2) I think.. where n should be max(len(a), len(b))
    # while loop takes place n times
    # str to int convertion generally takes O(n), but in this case every time only
    # 1 char is converted, so I think it should be O(1)
    # slicing takes O(n) 
    
    # SC: O(max(len(a), len(b)))
    # to keep the ans
