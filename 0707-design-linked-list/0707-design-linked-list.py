class Node:
    def __init__(self, value = 0 , nxt = None):
        self.value = value
        self.nxt = nxt

class MyLinkedList:

    def __init__(self):
        self.dummy = Node()
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        
        curr = self.dummy.nxt
        
        for _ in range(index):
            curr = curr.nxt
        
        return curr.value

    def addAtHead(self, val: int) -> None:
        v =self.addAtIndex(0, val)
        #print(self.size, v)
        
    def addAtTail(self, val: int) -> None:
        v= self.addAtIndex(self.size, val)
        #print(self.size, v)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return -1
        
        prev =  self.dummy
        curr = self.dummy.nxt
        
        for i in range(index):
            prev = curr
            curr = curr.nxt
        
        add = Node(val)
        add.nxt = curr
        prev.nxt = add
        self.size += 1
        #self.printFun()
    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return -1
        prev =  self.dummy
        curr = self.dummy.nxt
        
        for i in range(index):
            prev = curr
            curr = curr.nxt
        
        prev.nxt = prev.nxt.nxt
        self.size -=1
        #self.printFun()
    def printFun(self):
        curr = self.dummy.nxt
        
        while curr:
            print(curr.value, end=" ")
            curr = curr.nxt
        print("")


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)