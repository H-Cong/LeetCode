class BrowserHistory:

    def __init__(self, homepage: str):
        self.h = [homepage]
        self.i = 0

    def visit(self, url: str) -> None:
        self.h = self.h[:self.i+1]
        self.h.append(url)
        self.i+=1

    def back(self, steps: int) -> str:
        home = self.h
        if self.i - steps >= 0:
            self.i -= steps   
        else:
            self.i = 0
        return home[self.i]
        
        

    def forward(self, steps: int) -> str:
        home = self.h
        if self.i + steps <= len(home) - 1:
            self.i += steps   
        else:
            self.i = len(home) - 1
        return home[self.i]
    
    # TC: O(n)
    
    # SC: O(n)
            


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
