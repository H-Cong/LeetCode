class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        '''
        Stack: i serves as the last index of stack
        '''
        if len(asteroids) <= 1: return asteroids
        n = len(asteroids)
        i, j = 0, 1
        while j < n:
            if i < 0 or asteroids[i] < 0 or asteroids[j] > 0:
                i += 1
                asteroids[i] = asteroids[j]
                j += 1
            elif asteroids[i] < -asteroids[j]:
                i -= 1
            elif asteroids[i] == -asteroids[j]:
                i -= 1
                j += 1
            else:
                j += 1
                
        return asteroids[:i+1]
        
    # TC: O(n)
    # we scan the whole list, which is O(n).
    
    # SC: O(1)
    
    # ref: https://leetcode.com/problems/asteroid-collision/discuss/388154/Python-Solution-without-stack(Space%3A-O(1))-with-comments
