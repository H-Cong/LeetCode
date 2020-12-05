class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        Gradient Descent
        '''
        ans = random.randint(1,100)
        lr = 0.00001
        while abs(ans**2 - x) > 0.1: # 1
            ans -= lr * (ans**2 - x)
            # ans -= lr*4*ans*(ans**2-x)
        
        return int(ans+1) if int(ans+1)**2 == x else int(ans)
    
    # This GD solution is sensitive to learning rate
    
    # 1. you can also use 0.01, 0.001, 0.0001 etc
    #    the smaller the convergence condition, the longer it takes to run
    
    # ref: https://blog.csdn.net/weixin_39244297/article/details/108772358
