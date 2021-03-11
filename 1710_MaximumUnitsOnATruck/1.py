class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x:x[1], reverse = True)
        n = truckSize
        ans = 0
        for i in range(len(boxTypes)):
            if n > boxTypes[i][0] >= 0:
                ans += boxTypes[i][0] * boxTypes[i][1]
                n -= boxTypes[i][0]
            else:
                ans += n * boxTypes[i][1]
                return ans
        
        return ans
    
    # TC: O(nlogn)
    
    # SC: O(1)
