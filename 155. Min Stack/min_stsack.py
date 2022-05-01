class MinStack:

    def __init__(self):
        self.stack =[]
    def push(self, val: int) -> None:
        self.stack.append(val)
    def pop(self) -> None:
        self.stack.pop()        
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        new_list=[]
        for i in self.stack:
            new_list.append(i)
        new_list.sort()
        return new_list[0]

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(5)
obj.push(4)
obj.push(-4)
obj.pop()
param_3 = obj.top()
print(param_3)
param_4 = obj.getMin()
print(param_4)