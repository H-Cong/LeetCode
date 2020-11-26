class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        seen = {}
        seen[start] = arr[start]
        self.helper(start, arr, seen)
        
        
        return 0 in seen.values()
        
    
    def helper(self, index, arr, seen):
        if arr[index] == 0: return
        if index - arr[index] >= 0:
            if index - arr[index] not in seen:
                seen[index - arr[index]] = arr[index - arr[index]]
                self.helper(index - arr[index], arr, seen)
        if index + arr[index] < len(arr):
            if index + arr[index] not in seen:
                seen[index + arr[index]] = arr[index + arr[index]]
                self.helper(index + arr[index], arr, seen)
                
    # TC: O(n)
    # in worst case it will traverse all items in arr
    
    # SC: O(n)
    # worst case all items will be stored in dict and recursion happens n times, thus 2n??
    # worst case the DFS tree is linear, thus the height of the tree is n, best case the tree is balanced, where height is log(n)
    # thus stack space taken by recursion is between log(n) and n
