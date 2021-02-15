class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.msg_set = set()
        self.queue = deque()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        while self.queue:
            msg, t = self.queue[0]
            if timestamp - t >= 10:
                self.queue.popleft()
                self.msg_set.remove(msg)
            else:
                break
        if message not in self.msg_set:
            self.msg_set.add(message)
            self.queue.append((message, timestamp))
            return True
        else: 
            return False
        
    # TC: O(n)
    # n is the size of the queue. In worst case, all the messages in the queue become obsolete.
    
    # SC: O(n)
    # n is the size of the queue/set. it is actually 2n. but O(n) is complexity.

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
