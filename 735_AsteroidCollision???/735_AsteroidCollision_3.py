class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        '''
        Stack
        '''
        ans = []
        for new in asteroids:
            if new > 0:
                ans.append(new)
            else:
                while ans and 0 < ans[-1] < -new:
                    ans.pop()
                if not ans or ans[-1] < 0:
                    ans.append(new)
                elif ans[-1] == -new:
                    ans.pop()
                    
        return ans
    
    # TC: O(n)
    
    # SC: O(n)
    
