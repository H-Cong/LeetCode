class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if not asteroids or len(asteroids) == 1: return asteroids
        n = len(asteroids)
        i = 0
        while i < n - 1:
            if asteroids[i] > 0 and asteroids[i+1] < 0:
                if abs(asteroids[i]) > abs(asteroids[i+1]):
                    asteroids.pop(i+1)
                    n -= 1
                    continue
                elif abs(asteroids[i]) < abs(asteroids[i+1]):
                    asteroids.pop(i)
                    n -= 1
                    if i > 0:
                        i -= 1
                    continue
                else:
                    asteroids.pop(i+1)
                    asteroids.pop(i)
                    if i > 0:
                        i -=1
                    n -= 2
                    continue
            i += 1
        
        return asteroids
        
    # TC: O(n^2)???
    # we scan the whole list, which is O(n). And .pop() takes O(n)???
    
    # SC: O(1)
    
