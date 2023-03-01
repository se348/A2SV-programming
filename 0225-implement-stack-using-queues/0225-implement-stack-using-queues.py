class MyStack:

    def __init__(self):
        self.stack = []
        self.length = 0
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        self.length += 1

    def pop(self) -> int:
        popped = self.stack.pop()
        self.length -= 1
        return popped
    
    def top(self) -> int:
        if self.length == 0:
            return -1
        return self.stack[self.length - 1]

    def empty(self) -> bool:
        return not self.length
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()