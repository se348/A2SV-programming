class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [-1] * k
        self.front = 0
        self.rear =  -1
        self.size = k
        self.curr_size = 0
        
    def enQueue(self, value: int) -> bool:
        if self.curr_size == self.size:
            return False
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        self.curr_size += 1
        
        return True    
    
    def deQueue(self) -> bool:
        if self.curr_size == 0:
            return False
        
        self.queue[self.front] = -1
        self.front = (self.front +1) % self.size
        self.curr_size -= 1 
        
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]
    
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]
    
    def isEmpty(self) -> bool:
        return self.curr_size == 0
    
    def isFull(self) -> bool:
        return self.curr_size == self.size

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()