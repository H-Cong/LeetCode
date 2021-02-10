class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.queue = deque()
        self.window_sum = 0
        self.count = 0

    def next(self, val: int) -> float:
        self.count += 1
        self.queue.append(val)
        tail = self.queue.popleft() if self.count > self.size else 0
        self.window_sum = self.window_sum - tail + val
        
        return self.window_sum / min(self.size, self.count)
    
    # TC: O(1) 
    
    # SC: O(n) n is the size of the moving window


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
