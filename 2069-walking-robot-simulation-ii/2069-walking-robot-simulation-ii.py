class Robot:

    def inbound(self, x,y, width, height):
        return 0 <= x < width and 0 <= y < height
        
    def __init__(self, width: int, height: int):
        self.cycle = (2 * width) + (2 * height) - 4
        self.movement = {}
        self.direction = {}
        self.curr_dir = [0, 1]
        self.curr_cord = [0, -1]
        self.curr_num = 0
        self.trav = False
        
        for i in range(self.cycle + 1):
            
            
            if self.inbound(self.curr_dir[0] + self.curr_cord[0], self.curr_dir[1] + self.curr_cord[1], height, width):
                self.curr_cord[0] += self.curr_dir[0]
                self.curr_cord[1] += self.curr_dir[1]
            else:
                self.curr_dir[0], self.curr_dir[1] = self.curr_dir[1], self.curr_dir[0]
                self.curr_dir[1] *= -1
                self.curr_cord[0] += self.curr_dir[0]
                self.curr_cord[1] += self.curr_dir[1]
                
            self.movement[i] = self.curr_cord.copy()
            self.direction[i] = self.curr_dir.copy()
        
    def step(self, num: int) -> None:
        self.trav = True
        self.curr_num = (self.curr_num + num) % self.cycle
        

    def getPos(self) -> List[int]:
        temp1, temp0 = self.movement[self.curr_num]
        return [temp0, temp1]

    def getDir(self) -> str:
        if not self.trav and not self.curr_num:
            return "East"
        elif not self.curr_num:
            return "South"
        elif self.direction[self.curr_num] == [0, 1]:
            return "East"
        elif self.direction[self.curr_num] == [1, 0]:
            return "North"
        elif self.direction[self.curr_num] == [0, -1]:
            return "West"
        
        return "South"


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()