class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # for more info look at Problem 692 py files
        count = collections.Counter(nums)
        candidates = list(count)
        candidates.sort(key=lambda x:-count[x])
        
        return candidates[:k]
    
    # TC: O(nlogn)
    
    # SC: O(n)
