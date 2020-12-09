class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        '''
        Backtrack
        '''
        res = []
        self.backtrack(res, 1, n, k, [])
        return res
    
    def backtrack(self, res, first, n, k, curr):
        if len(curr) == k:
            res.append(curr[:])
        for i in range(first, n+1):
            curr.append(i)
            self.backtrack(res, i + 1, n, k, curr)
            curr.pop()
    
    # TC: O(kC_n^k)
    
    # SC: O(C_n^k)
