class MyCircularDeque:

    def __init__(self, k: int):
        self.size =k
        self.custom_queue =[]

    def insertFront(self, value: int) -> bool:
        if len(self.custom_queue)==self.size:
            return False
        self.custom_queue.insert(0, value)
        return True
    def insertLast(self, value: int) -> bool:
        if len(self.custom_queue)==self.size:
            return False
        self.custom_queue.append(value)
        return True

    def deleteFront(self) -> bool:
        if len(self.custom_queue)==0:
            return False
        self.custom_queue.pop(0)
        return True
    def deleteLast(self) -> bool:
        if len(self.custom_queue)==0:
            return False
        self.custom_queue.pop()
        return True

    def getFront(self) -> int:
        if len(self.custom_queue)==0:
            return -1
        return self.custom_queue[0]

    def getRear(self) -> int:
        if len(self.custom_queue)==0:
            return -1
        return self.custom_queue[-1]

    def isEmpty(self) -> bool:
        return len(self.custom_queue)==0        

    def isFull(self) -> bool:
        return len(self.custom_queue)==self.size


# Your MyCircularDeque object will be instantiated and called as such:
myCircularDeque =MyCircularDeque(3)
print(myCircularDeque.insertLast(1));  
print(myCircularDeque.insertLast(2));  
print(myCircularDeque.insertFront(3)); 
print(myCircularDeque.insertFront(4)); 
print(myCircularDeque.getRear());      
print(myCircularDeque.isFull());       
print(myCircularDeque.deleteLast());   
print(myCircularDeque.insertFront(4)); 
print(myCircularDeque.getFront());     