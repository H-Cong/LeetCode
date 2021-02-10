class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.queue = []

    def next(self, val: int) -> float:
        size, queue = self.size, self.queue
        queue.append(val)
        window_sum = sum(queue[-size:])
        
        return window_sum / min(len(queue), size)
    
    # TC: O(n) n is the size of the moving window
    
    # SC: O(m) m is the length of the queue which would grow at each invocation of the next(val) function.


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
