class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        
        if len(A) != len(B): return False
        if not A and not B: return True
        
        temp = deque()
        for i,c in enumerate(A):
            if c != B[0]:
                temp.append(c)
            else:
                temp.appendleft(A[i:])
                _A = ''.join(temp)
                if _A == B: return True
                temp.popleft() # this is for the case where duplicated char exists in string
                temp.append(c)
        
        return False
    
    # TC: O(n^2)??
    # for loop O(n), A[i:] O(n), _A==B O(n)
    
    # SC: O(n)
