class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalCuts.append(h)
        verticalCuts.append(w)
        x, y = horizontalCuts[0], verticalCuts[0]
        for i in range(1, len(horizontalCuts)):
            x = max(x, horizontalCuts[i] - horizontalCuts[i-1])
        for j in range(1, len(verticalCuts)):
            y = max(y, verticalCuts[j] - verticalCuts[j-1])
        
        
        return (x*y) % ((10 ** 9) + 7)
    
    # TC: O(nlongn) 
    # n is the max(len(horizontalCuts), len(verticalCuts))
    
    # SC: O(1)
            
