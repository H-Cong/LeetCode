class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res = 0
        for i in range(len(time)):
            for j in range(i+1, len(time)):
                if (time[i] + time[j]) % 60 == 0:
                    res += 1
        
        return res
    
    # TC: O(n^2)
    
    # SC: O(1)
    
    # TLE
