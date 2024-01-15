class StockSpanner:

    def __init__(self):
        self.nums = []
        self.count = []

    def next(self, price: int) -> int:
        if not self.nums or price < self.nums[-1]:
            self.nums.append(price)
            self.count.append(1)
            return 1
        
        count = 1
        while self.nums and self.nums[-1] <= price:
            self.nums.pop()
            count += self.count.pop()
            
        self.nums.append(price)
        self.count.append(count)
        
        return count
    
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)