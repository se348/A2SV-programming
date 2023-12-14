class Bitset:

    def __init__(self, size: int):
        self.arr = [0] * size
        self.size = size
        self.curr_count = 0
        self.reversed = False
        

    def fix(self, idx: int) -> None:
        if self.reversed:
            if self.arr[idx] == 1:
                self.curr_count -= 1
            self.arr[idx] = 0
        else:
            if self.arr[idx] == 0:
                self.curr_count += 1
            self.arr[idx] = 1
        
    def unfix(self, idx: int) -> None:
        if self.reversed:
            if self.arr[idx] == 0:
                self.curr_count += 1
            self.arr[idx] = 1
        else:
            if self.arr[idx] == 1:
                self.curr_count -= 1
            self.arr[idx] = 0
    def flip(self) -> None:
        self.reversed = not self.reversed
    def all(self) -> bool:
        
        if self.reversed:
            return self.curr_count == 0
        return self.curr_count == self.size
    
    def one(self) -> bool:
        
        if self.reversed:
            return self.curr_count != self.size
        return self.curr_count != 0

    def count(self) -> int:
        
        if self.reversed:
            return self.size - self.curr_count
        return self.curr_count

    def toString(self) -> str:
        if self.reversed:
            return "".join([str(1 - i) for i in self.arr])
        
        return "".join([str(i) for i in self.arr])

# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()