class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            row = [1] * (i+1) # construct a row for each row
            for j in range(1, i): # this loop wont be entered when i = 0 or 1
                row[j] = res[-1][j-1] + res[-1][j] # change the current row value
            res.append(row)
        return res
        
        # TC: O(n^2)
        # two for loops
        # or more precisely, we can calculate the total number of elements within this triangle
        # the sum formula it (n/2)*(a_1 + a_n), where a_1=1 and a_n = n
        
        # SC: O(n^2)
        # Because we need to store each number that we update in triangle, 
        # the space requirement is the same as the time complexity.
