class MyCircularDeque:

    def __init__(self, k: int):
        self.curr_size = 0
        self.size = k
        self.queue = [0] * k
        self.front = 0
        self.rear = -1
        
    def insertFront(self, value: int) -> bool:
        if self.curr_size == self.size:
            return False
        self.front = (self.front - 1) % self.size
        self.queue[self.front] = value
        self.curr_size += 1
        
        return True
    def insertLast(self, value: int) -> bool:
        
        if self.curr_size == self.size:
            return False
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        self.curr_size += 1
        return True

    def deleteFront(self) -> bool:
        if self.curr_size == 0:
            return False
        self.front = (self.front + 1) % self.size
        self.curr_size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.curr_size == 0:
            return False
        self.rear = (self.rear - 1) % self.size
        self.curr_size -= 1
        return True

    def getFront(self) -> int:
        if self.curr_size == 0:
            return -1
        return self.queue[self.front]

    def getRear(self) -> int:
        if self.curr_size == 0:
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        if self.curr_size == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.curr_size == self.size:
            return True
        return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()