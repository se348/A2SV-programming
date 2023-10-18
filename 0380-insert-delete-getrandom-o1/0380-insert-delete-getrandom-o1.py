class RandomizedSet:

    def __init__(self):
        self.dictionary = {}
        self.list = []
        
    def insert(self, val: int) -> bool:
        if val in self.dictionary:
            return False
        
        self.dictionary[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dictionary:
            return False
        
        changed = self.list[-1]
        to_be_removed = self.dictionary[val]
        self.dictionary[changed]= to_be_removed
        self.list[to_be_removed] = changed
        
        self.dictionary.pop(val)
        self.list.pop()
        return True
        
    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()