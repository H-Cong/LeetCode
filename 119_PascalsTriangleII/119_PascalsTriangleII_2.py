class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = []
        for i in range(rowIndex+1):
            row.insert(0, 1)
            for j in range(1, i):
                row[j]= row[j] + row[j+1]
        return row
    
    # TC: O(n^2)
    # same as the Pascal`s triangle problem 1
    # (n/2)*(1+n)
    
    # SC: O(n)
    # No extra space required other than that required to hold the output.
