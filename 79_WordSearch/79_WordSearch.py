class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board: return False
        row = len(board)
        col = len(board[0])
        
        for i in range(row):
            for j in range(col):
                if self._dfs(board, row, col, i, j, word, 0):
                    return True
        
        return False
    
    def _dfs(self, board, row, col, i, j, word, index):
        if index == len(word): return True

        if i < 0 or i >= row or j < 0 or j >= col or board[i][j] != word[index]:
            return False
        
        temp = board[i][j]
        board[i][j] = '#' # this is prevent same block being counted twice to fit the "unique" requirement
        
        found = self._dfs(board, row, col, i, j-1, word, index+1) \
                or self._dfs(board, row, col, i+1, j, word, index+1) \
                or self._dfs(board, row, col, i, j+1, word, index+1) \
                or self._dfs(board, row, col, i-1, j, word, index+1) 
        
        board[i][j] = temp
        
        return found
    
    # TC: O(n*3^L) where where n is the number of cells in the board and L is the length of the word to be matched.
    # For the backtracking function, initially we could have at most 4 directions to explore, but further the 
    # choices are reduced into 3 (since we won't go back to where we come from). As a result, the execution trace 
    # after the first step could be visualized as a 3-ary tree, each of the branches represent a potential
    # exploration in the corresponding direction. Therefore, in the worst case, the total number of invocation 
    # would be the number of nodes in a full 3-nary tree, which is about 3^L 
    
    # We iterate through the board for backtracking, i.e. there could be n times invocation for the backtracking
    # function in the worst case.
    
    # SC: O(L)
    # The main consumption of the memory lies in the recursion call of the backtracking function. The maximum 
    # length of the call stack would be the length of the word. Therefore, the space complexity of the algorithm 
    # is O(L).
    
            
                
