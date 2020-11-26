class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n) # cuz we dont know which one is longer
        carry = 0
        ans = ""
        
        for i in range(n - 1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1
            
            remainder = carry % 2
            ans = str(remainder) + ans
            
            carry //= 2
        
        if carry == 1:
            ans = str(carry) + ans
        
        return ans
    
    # TC: O(max(len(a), len(b))) I think.. 
    # while loop takes place max(len(a), len(b)) times
    
    # SC: O(max(len(a), len(b)))
    # to keep the ans
    
    # str.zfill(n) will add '0' at beginning of str untill len(str) reaches n
