class Solution:
    def canCross(self, stones: List[int]) -> bool:
        '''
        Brute Force
        '''
        return self.cross(stones, 0, 0)
    
    def cross(self, stones, ind, jumpsize):
        for i in range(ind+1, len(stones)):
            gap = stones[i] - stones[ind]
            if jumpsize-1 <= gap <= jumpsize+1:
                if self.cross(stones, i, gap):
                    return True
        
        return ind == len(stones) - 1
        
    # TC: O(3^n)
    # Recursion tree can grow upto 3^n.
    
    # SC: O(n) 
    # Recursion of depth nn is used.
    
    # TLE, mainly happens when n is large, and step size = 1 and jump successfully untill the last step.
