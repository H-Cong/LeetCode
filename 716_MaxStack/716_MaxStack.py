class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []

    def push(self, x: int) -> None:
        stack = self.s
        stack.append(x)

    def pop(self) -> int:
        stack = self.s
        res = stack[-1]
        del stack[-1]
        return res

    def top(self) -> int:
        stack = self.s
        return stack[-1]

    def peekMax(self) -> int:
        stack = self.s
        m = max(stack)
        return m

    def popMax(self) -> int:
        stack = self.s
        m = max(stack)
        for i in reversed(range(len(stack))):
            if stack[i] == m: 
                del stack[i] 
                break
        return m
    
    # TC: O(n)
    
    # SC: O(n)


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
