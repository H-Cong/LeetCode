class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not words: return None
        row = len(board)
        col = len(board[0])
        res = []
        for i in range(row):
            for j in range(col):
                for word in words:
                    if self._dfs(board, i, j, word, 0, res) and word not in res:
                        res.append(word)
        
        return res
    
    def _dfs(self, board, row_index, col_index, word, index, res):
        
        row = len(board)
        col = len(board[0])
        
        if row_index < 0 or row_index >= row or col_index < 0 or col_index >= col or word[index] != board[row_index][col_index]:
            return False
        if index == len(word)-1:
            return True
        
        
        temp = board[row_index][col_index]
        board[row_index][col_index] = '#'
        
        Found = self._dfs(board, row_index, col_index-1, word, index+1, res) \
            or self._dfs(board, row_index+1, col_index, word, index+1, res) \
            or self._dfs(board, row_index, col_index+1, word, index+1, res) \
            or self._dfs(board, row_index-1, col_index, word, index+1, res)
        
        board[row_index][col_index] = temp
        
        return Found
    
    # TC: O(sum(m*n*4*3^(L-1))) 
    # sum is the total number of words in the words list
    # m is the row, n is the col, L is the maximum length of words
    
    # SC: O(L)
    # L: length of the longest word in words. i.e. length of maximum recursive call
    
    # NOTE: we could use Trie to speed up the algorithm with the cost of more space. I didn`t study the Trie yet
    # so maybe some time later I will look into that solution
        
