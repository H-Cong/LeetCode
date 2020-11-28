class Solution:
    def canCross(self, stones: List[int]) -> bool:
        '''
        DP
        '''
        if stones[1] != 1: return False # as in description, len(stones) >= 2
            
        d = {s:set() for s in stones}  #  a set does not hold duplicates
        d[1].add(1)
        
        for s in stones[:-1]:
            for jump in d[s]:
                for k in [jump + 1, jump, jump - 1]:
                    if k > 0 and s + k in d:
                        d[s+k].add(k)
        
        return bool(d[stones[-1]])
    
    # TC: O(n^2)
    # outer for loop: O(n)
    # mid for loop: O(n) is the upper bound, in theory, 
    # it should be O(sqrt(n)) according to post under LC official solution
    # inner for loop: O(3), wont alter the overall TC
    
    # SC: O(n^2) 
    # hashmap size can grow upto n^2. Again, I suspect this is a upper bound.
