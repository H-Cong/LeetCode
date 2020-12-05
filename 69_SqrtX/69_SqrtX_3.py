class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        Gradient Descent with Adaptive Learning Rates
        '''
        n = 0
        lr = x
        while abs(n**2 - x) >= 0.1:
            lr = lr / 2
            gradient = self._gradient(x, n)
            n -= lr*gradient
        
        return int(n + 1) if int(n + 1)**2 == x else int(n)
    
    def _gradient(self, x, n):
        v = n**2 - x
        return 1 if v > 0 else -1
    
    # TC: log(x)
    
    # SC: O(1)

    # why starts from 0? 
    # I think as f(x) = x^2 - n where n >= 0 is monotonically increaseing in
    # the range of [0, inf). And we are looking for the point to make f(x) = 0
    # When gradient (i.e. f(x)) < 0, it means that we need to move x to right
    # When gradient > 0, it means that the target x is on the left of current x
    # Initializing x = 0 is the only way to make this logic valid.
    
    # ref: https://leetcode.com/problems/sqrtx/discuss/869428/Gradient-Descent-solution-for-machine-learning-interviews-O(logx)
