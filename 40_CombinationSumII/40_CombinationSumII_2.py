class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        Backtracking
        '''
        candidates.sort()
        if sum(candidates) < target: return None
        self.res = set()
        self.backtrack(candidates, target, [], 0)
        return self.res
    
    def backtrack(self, candidates, target, curr, start):
        if target == 0:
            self.res.add(tuple(curr))  # 1
            return
        if target < 0:
            return
        
        for i in range(start, len(candidates)):
            curr.append(candidates[i])
            new_target = target - candidates[i]
            self.backtrack(candidates, new_target, curr, i+1) # 2
            curr.pop()
            
    # TC: O(2^n)
    
    # SC: O(kn)
    
    # NOTE: how this is different from 39 is that 
    # 1. we need check whether a combination has already been in res
    # 2. we need to add 1 to start index everytime to avoid using same element 
    #    multiple times
    
    # ref: https://www.youtube.com/watch?v=RSatA4uVBDQ
