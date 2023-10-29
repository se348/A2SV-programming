class DetectSquares:

    def __init__(self):
        self.curr_count = defaultdict(int)
        self.x = defaultdict(list)
        self.y = defaultdict(list)

    def add(self, point: List[int]) -> None:
        tuple_ver = tuple(point)
        
        self.curr_count[tuple_ver] += 1
        
        if self.curr_count[tuple_ver] == 1:
            self.x[point[0]].append(point[1])
            self.y[point[1]].append(point[0])
        
        
    def count(self, point: List[int]) -> int:
        res = 0
        
        for j0 in self.x[point[0]]:
            for i0 in self.y[point[1]]:

                if j0 == point[1] or i0 == point[0]:
                    continue
                
                diff1 = abs(point[0] -  i0)
                diff2 = abs(point[1] - j0)
                
                if diff1 != diff2:
                    continue
                
                a = self.curr_count[(point[0], j0)]
                b = self.curr_count[(i0, point[1])]
                c = self.curr_count[(i0, j0)]
                
                res += (a * b * c)
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)