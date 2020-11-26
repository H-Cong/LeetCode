from collections import defaultdict, Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # in order to solve this in O(nlogk) we will have to use Priority Queue (min heap)
        # I need to do some study on this
        # the following is the solution from Problem 347 Top K Frequent Elements
        # this does not work as now we have to consider the alphabetical order as well
        
        # 1. build hash map : character and how often it appears
        # O(N) time
        count = Counter(words)   
        # 2-3. build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        return heapq.nlargest(k, count.keys(), key=count.get) 
