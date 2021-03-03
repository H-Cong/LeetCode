# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        d = binaryMatrix.dimensions()
        r, c = d[0], d[1]
        ans = -1
        for i in range(r):
            for j in reversed(range(c)):
                if binaryMatrix.get(i, j) == 1:
                    ans = j
                    c = j
                else:
                    break
        
        return ans
    
    # TC: O(r+c)
    
    # SC: O(1)
                    
                
