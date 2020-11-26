class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        seen = set()
        seen.add(start)
        return self.helper(start, arr, seen)
        
    def helper(self, index, arr, seen):
        if arr[index] == 0: return True
        if index - arr[index] >= 0:
            if index - arr[index] not in seen:
                seen.add(index - arr[index])
                if self.helper(index - arr[index], arr, seen): # this if statement is to make sure even left child return false, we still can check right child
                    return True
        if index + arr[index] < len(arr):
            if index + arr[index] not in seen:
                seen.add(index + arr[index])
                return self.helper(index + arr[index], arr, seen)
            
        return False
                
    # TC: O(n)
    # in worst case it will traverse all items in arr
    
    # SC: O(n)
    # worst case all items will be stored in dict and recursion happens n times, thus 2n?? 
