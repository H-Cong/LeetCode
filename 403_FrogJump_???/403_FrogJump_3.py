class Solution:
    def canCross(self, stones: List[int]) -> bool:
        '''
        DFS
        '''
        if stones[1] != 1: return False
        
        for i in range(len(stones)): # early termination
            if i > 0 and stones[i] - stones[i-1] > i:
                return False
        
        stone_set = set(stones)
        dest = stones[-1]
        lastJump = 1
        currStone = 1
        
        return self.cross(stone_set, currStone, lastJump, dest)
        
    def cross(self, stone_set, currStone, lastJump, dest):
        if lastJump <= 0: return False
        if currStone not in stone_set: return False
        if currStone == dest: return True
        
        return self.cross(stone_set, currStone + lastJump + 1, lastJump + 1, dest) or \
               self.cross(stone_set, currStone + lastJump, lastJump, dest) or \
               self.cross(stone_set, currStone + lastJump - 1, lastJump - 1, dest)
        
    
    # TC: I dont know tbh..
    
    # SC: O(n) for set(), O(???) for recursion??
    
    # NOTE:
    # 1. Pre-check for early termination is necessary (otherwise Time Limit Exceed)
    # i is the largest step possible so far to reach stone[i-1] as is a 0 based index
    # thus stones[i] will be too far to be reached if distance between stone i and i-1 > i
    # 2. During DFS, we should try to jump as far as we can cause this strategy is more 
    # likely to reach the destination. Therefore we should try unit+preStep+1 then unit+preStep 
    # and finally unit+preStep-1. If we try unit+preStep-1 first, it will be Time Limit Exceed,
    # even with pre-checked enabled
    
    # ref: https://leetcode.com/problems/frog-jump/discuss/264202/Something-that-you-may-not-realize-about-BFS-and-DFS-solution

