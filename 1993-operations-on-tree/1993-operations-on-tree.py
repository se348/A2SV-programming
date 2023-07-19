class LockingTree:

    def __init__(self, parent: List[int]):
        
        self.parent = parent
        self.descendant = defaultdict(list)
        self.locker = [-1] * len(parent)
        
        for ind, val in enumerate(parent):
            
            self.descendant[val].append(ind)
            

    def lock(self, num: int, user: int) -> bool:
        if self.locker[num] != -1:
            return False
        
        self.locker[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.locker[num] != user:
            return False
        
        self.locker[num] = -1
        return True
    
    def checkIsAncestorsUnlocked(self, ind) -> bool:
        
        if ind == -1:
            return True
        
        if self.locker[ind] == -1:
            return self.checkIsAncestorsUnlocked(self.parent[ind])
        return False
    
    def checkIsAnyDescendantLocked(self, ind) -> bool:
        childs = deque()
        for el in self.descendant[ind]:
            childs.append(el)
        
        while childs:
            
            child = childs.popleft()
            
            if self.locker[child] != -1:
                return True
            
            for nextChild in self.descendant[child]:
                childs.append(nextChild)
        
        return False
        
    def upgrade(self, num: int, user: int) -> bool:
        if not self.checkIsAncestorsUnlocked(num):
            return False
        
        if not self.checkIsAnyDescendantLocked(num):
            return False
        
        self.locker[num] = user
        
        queue = deque()
        
        for child in self.descendant[num]:
            queue.append(child)
            
        while queue:
            
            curr = queue.popleft()
            
            self.locker[curr] = -1
            
            for child in self.descendant[curr]:
                queue.append(child)
                
        return True


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)