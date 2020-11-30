class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for new in asteroids:
            while ans and new < 0 < ans[-1]:
                if ans[-1] < -new:
                    ans.pop()
                    continue
                elif ans[-1] == -new:
                    ans.pop()
                break  # 1
            else:
                ans.append(new)
        return ans
    
    # TC: O(n)
    
    # SC: O(n)
    
    # 1. break when ans[-1] > -new where new will disappear, so we just continue with the 
    #    next new asteroid
        
