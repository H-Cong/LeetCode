class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        HashSet
        '''
        seen = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    curr = board[i][j]
                    if (i, curr) in seen or (curr, j) in seen or (i//3, j//3, curr) in seen:
                        return False
                    seen.add((i, curr))
                    seen.add((curr, j))
                    seen.add((i//3, j//3, curr))
                    
        return True
    
    # TC: O(1)
    # since all we do here is just one iteration over the board with 81 cells
    
    # SC: O(1)
    
    # ref: https://leetcode.com/problems/valid-sudoku/discuss/15509/Clean-and-Easy82ms-Python
