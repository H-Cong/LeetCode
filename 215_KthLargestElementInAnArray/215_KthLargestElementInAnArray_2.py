class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        return heapq.nlargest(k, nums)[-1]
    
    # TC: O(nlogk)
    
    # SC: O(k)
    # to store the heap elements
