class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        '''
        DP
        '''
#         A = [1] + nums + [1]
#         return self.dp(A, 0, len(A)-1)
    
#     @lru_cache(None)
#     def dp(self, A, i, j):
#         return max([A[i]*A[k]*A[j] + self.dp(A, i, k) + self.dp(A, k, j) for k in range(i+1, j)] or [0])

        A = [1] + nums + [1]
        
        @lru_cache(None)
        def dfs(i, j):
            return max([A[i]*A[k]*A[j] + dfs(i,k) + dfs(k,j) for k in range(i+1, j)] or [0])
        
        return dfs(0, len(A) - 1)
    
    # TC: O(n^3)
    
    # SC: O(n^2)
    
    # ref: https://leetcode.com/problems/burst-balloons/discuss/970727/Python-5-lines-dp-explained
    # ref: https://docs.python.org/3/library/functools.html#functools.cache
    # ref: https://docs.python.org/3/library/functools.html#functools.lru_cache
