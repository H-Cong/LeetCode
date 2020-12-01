class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        '''
        DFS
        '''
        res = []
        self.dfs(res, 1, 9, n)
        return res
    
    def dfs(self, res, start, end, dest):
        while start <= end and start <= dest:
            res.append(start)
            self.dfs(res, start*10, start*10 + 9, dest)
            start += 1
            
    # TC: O(n)
    # I think it will just go through every int from 1 to n once
    
    # SC: O(n)
    # space that res takes. As for the recursion, it should have the number of digit of n recursions.
    # e.g. if n = 112, then recursion is a 3 level recursion.
    
    # ref: https://leetcode.com/problems/lexicographical-numbers/discuss/399796/EasyandSimple-recursion-beats-100-!-Explanation-%2B-Graphic-Illustration-Included
