class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.backtrack(res, "", 0, 0, n)
        return res
    
    def backtrack(self, res, curr_string, _open, _close, _max):
        if len(curr_string) == 2*_max:
            res.append(curr_string)
            return
        
        if _open < _max:
            self.backtrack(res, curr_string+"(", _open+1, _close, _max)
        if _close < _open:
            self.backtrack(res, curr_string+")", _open, _close+1, _max)
        
    # TC: O((4^n/n^1.5)*(n)) = O(4^n/sqrt(n))
    # Each valid sequence has at most n steps during the backtracking procedure.
    
    # SC:  O(4^n/sqrt(n))
    # as described above, and using O(n) space to store the sequence.
    
    '''
    Generating all combinations of well formed paranthesis is a typical example of catalan numbers. 
    You can use the links at the bottom here if you are not aware of the catalan numbers since they 
    are at the heart of the exercise.
    
    Let time complexity for the generating all combinations of well-formed parentheses is f(n), then
    f(n) = g(n) * h(n) where g(n) is the time complexity for calculating nth catalan number, and h(n) 
    is the time required to copy this combination to result array.

    Therefore, f(n) = catalan(n) * O(n) which is O(4^n/n^1.5)*(n)). Broadly saying just remember that 
    this is a typical example of catalan number and it's time complexity is similar to how catalan(n) is got.
    
    Further readings in to catalan numbers:
    https://en.wikipedia.org/wiki/Catalan_number
    https://www.youtube.com/watch?v=GlI17WaMrtw
    https://www.youtube.com/watch?v=eoofvKI_Okg
    '''
