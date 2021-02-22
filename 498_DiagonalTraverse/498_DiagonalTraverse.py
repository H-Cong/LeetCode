class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]: return None
        d = collections.defaultdict(list)
        m, n = len(matrix), len(matrix[0])
        ans = []
        for i in range(m):
            for j in range(n):
                d[i+j].append(matrix[i][j])
        for entry in d.items():
            if entry[0] % 2 == 0:
                ans.extend(entry[1][::-1])
            else:
                ans.extend(entry[1])
        return ans
    
    # TC: O(m*n)
    
    # SC: O(m*n)
    
    # since python 3.6, the order of items in dict is guaranteed.
    # ref: https://leetcode.com/problems/diagonal-traverse/discuss/581868/Easy-Python-NO-DIRECTION-CHECKING
