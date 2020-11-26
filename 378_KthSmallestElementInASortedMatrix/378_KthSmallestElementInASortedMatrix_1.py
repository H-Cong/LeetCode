class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        flatList = [j for sub in matrix for j in sub]
        flatList.sort()
        
        return flatList[k-1]
    
    # TC: O(n^2) where n is the number of rows
    # n^2 to generate flatList, nlogn to sort
    
    # SC: O(n^2)
