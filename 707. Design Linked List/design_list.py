class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self , head=None):
        self.head = head
        
    def get(self, index: int) -> int:
        i= 0
        tempo = self.head
        while i< index:
            if not tempo:
                return -1
            tempo =tempo.next
            i+=1
        return tempo.val if tempo else -1
    def addAtHead(self, val: int) -> None:
        listNode = ListNode()
        listNode.val =val
        listNode.next =self.head
        self.head = listNode

    def addAtTail(self, val: int) -> None:
        if self.head ==None:
            listNode = ListNode()
            listNode.val =val
            self.head =listNode
            return
        tempo = self.head
        node =self.head
        while tempo:
            node =tempo
            tempo = tempo.next
        listNode = ListNode()
        listNode.val =val
        node.next = listNode

    def addAtIndex(self, index: int, val: int) -> None:
        i= 0
        tempo = self.head
        curr = self.head
        if index>0:
            while i< index:
                curr = tempo
                if not tempo:
                    return
                tempo =tempo.next
                i+=1        
            listNode =ListNode()
            listNode.val =val
            listNode.next = tempo
            curr.next = listNode
        if index==0:
            listNode =ListNode()
            listNode.val =val
            listNode.next = self.head
            self.head =listNode
    def deleteAtIndex(self, index: int) -> None:
        i= 0
        tempo = self.head
        curr = self.head
        if index== 0:
            self.head = self.head.next
        while i< index:
            curr = tempo
            if not tempo:
                return 
            tempo =tempo.next
            i+=1  
        if curr and tempo:
            curr.next = tempo.next