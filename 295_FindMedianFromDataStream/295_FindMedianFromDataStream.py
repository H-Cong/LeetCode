# from heapq import *
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lo = [] # is a max_heap
        self.hi = [] # is a min_heap

    def addNum(self, num: int) -> None:
        heappush(self.lo, -num) # since python default deap is min_heap, thus we *(-1) to make it max_heap
        heappush(self.hi, -self.lo[0]) # multiply by another -1 to revert the sign
        heappop(self.lo)
        
        if len(self.hi) > len(self.lo):
            heappush(self.lo, -self.hi[0])
            heappop(self.hi)

    def findMedian(self) -> float:
        if len(self.lo) > len(self.hi):
            return -self.lo[0]
        else:
            return (self.hi[0] - self.lo[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


    # TC: O(5*logn) + O(1) n is the number of elements hold in one heap
    # At worst, there are three heap insertions and two heap deletions 
    # from the top. Each of these takes about O(logn) time.
    # Finding the median takes constant O(1) time since the tops of 
    # heaps are directly accessible.
    
    # SC: O(n)
    # linear space to hold input in containers.
    
    # ref: https://leetcode.com/problems/find-median-from-data-stream/discuss/696658/Python-Logic-Explained-with-2-Heaps-Clean-code.
    
    
    
