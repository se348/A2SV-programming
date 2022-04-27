from numpy import true_divide


class MyQueue:

    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def push(self, x: int) -> None:
        self.stack1.append(x)
    def pop(self) -> int:
        if self.empty():
            return None
        while len(self.stack1) !=1:
            last =self.stack1.pop()
            self.stack2.append(last)
        end= self.stack1.pop()
        while len(self.stack2) != 0:
            value =self.stack2.pop()
            self.stack1.append(value)
        return end
    def peek(self) -> int:
        if self.empty():
            return None
        while len(self.stack1) !=1:
            last =self.stack1.pop()
            self.stack2.append(last)
        end= self.stack1.pop()
        self.stack2.append(end)
        while len(self.stack2) != 0:
            value =self.stack2.pop()
            self.stack1.append(value)
        return end
    def empty(self) -> bool:
        if len(self.stack1)==0:
            return True
        return False
        


obj = MyQueue()
obj.push(1)
obj.push(4)
param_2 = obj.pop()
print(param_2)
param_3 = obj.peek()
print(param_3)
param_4 = obj.empty()
print(param_4)
