class Solution:
    def countBits(self, num: int) -> List[int]:
        '''
        DP
        '''
        res = [0]*(num+1)
        for i in range(num+1):
            res[i] = res[i>>1] + (i&1)
        
        return res
    
    # TC: O(n)
    
    # SC: O(n)
    
    # ref: https://leetcode.com/problems/counting-bits/discuss/270693/Intermediate-processsolution-for-the-most-voted-solution-i.e.-no-simplificationtrick-hidden
    # ref: https://leetcode.com/problems/counting-bits/discuss/656539/Python-Clean-dp-solution-O(n)-beats-99-with-explanations.
