class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        '''
        HashMap
        '''
        remainders = collections.defaultdict(int)
        res = 0
        for t in time:
            if t % 60 == 0:
                res += remainders[0]
            else:
                res += remainders[60-t%60]
            remainders[t%60] += 1
        
        return res
    
    # TC: O(n)
    
    # SC: O(1) because the size of the array remainders is fixed with 60
    
    # ref: https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/solution/
    
    
