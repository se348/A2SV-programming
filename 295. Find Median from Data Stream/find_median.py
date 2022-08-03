import heapq


class MedianFinder:

    def __init__(self):
        self.small=[]
        self.large =[]
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        self.balance()
        if self.large!=[] and self.small!=[] and ((-1 * self.small[0]) > self.large[0]):
            val1 = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val1)
            self.balance()
    def balance(self):
        if self.check() ==1:
            heapq.heappush(self.large,-1 * heapq.heappop(self.small))
        elif self.check() ==-1:
            heapq.heappush(self.small,-1 * heapq.heappop(self.large))
        
        
    def check(self):
        if abs(len(self.small) -len(self.large)) <2:
            return 0
        if len(self.small) -len(self.large) >1:
            return 1
        return -1
    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return ((-1 * self.small[0]) + self.large[0])/2
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        else: return self.large[0] 


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()