class DataStream:

    def __init__(self, value: int, k: int):
        
        self.nums = []
        self.value = value
        self.k = k
        self.lastDifferent = None
    def consec(self, num: int) -> bool:
        
        if num != self.value:
            self.lastDifferent = len(self.nums)
        self.nums.append(num)
        if len(self.nums) < self.k:
            return False
        elif self.lastDifferent is None:
            return True
        elif len(self.nums) - self.lastDifferent > self.k:
            return True
        return False

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)