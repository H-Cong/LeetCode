class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        for i in range(rowIndex + 1): # NOTE here one needs to add 1
            row = [1] * (i + 1) # add 1 here as well
            for j in range(1, i):
                row[j] = res[-1][j-1] + res[-1][j]
            res.append(row)
        
        return res[-1]
    
    # TC: O(n^2)
    # two for loops
    # or more precisely, we can calculate the total number of elements within this triangle
    # the sum formula it (n/2)*(a_1 + a_n), where a_1=1 and a_n = n

    # SC: O(n^2)
    # Because we need to store each number that we update in triangle, 
    # the space requirement is the same as the time complexity.
