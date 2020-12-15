class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        Backtracking
        '''
        res = []
        self.backtrack(candidates, target, res, [], 0)
        return res
    
    def backtrack(self, candidates, target, res, curr, start):
        if target == 0:
            # res.append(curr) # NOTE
            res.append(list(curr))
            return
        elif target < 0:
            return
        
        for i in range(start, len(candidates)):
            curr.append(candidates[i])
            new_target = target - candidates[i]
            self.backtrack(candidates, new_target, res, curr, i)
            curr.pop()
            
    
    # TC: O(n^(t/m + 1))
    # n is the number of candidates, t is the target value, m is the minimal value among the candidates
    
    # SC: O(t/m)
    
    # NOTE: list(curr) makes a deepcopy of curr. If we just use curr instead of list(curr), then 
    # whenever curr elements changes, res will also change
    
    # ref: https://leetcode.com/problems/combination-sum/solution/
