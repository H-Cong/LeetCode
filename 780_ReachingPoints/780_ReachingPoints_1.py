class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        '''
        Work Backwards. Greedy???
        '''
        while tx >= sx and ty >= sy:
            if sx == tx and sy == ty: return True
            if tx > ty: tx -= ty
            else: ty -= tx
        
        return False
    
    # TC: O(max(tx, ty))
    # If say ty = 1, we could be subtracting tx times.
    
    # SC: O(1)

    # ref: https://leetcode.com/problems/reaching-points/solution/
