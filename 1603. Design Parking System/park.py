class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        
        self.bigSpace = big
        self.mediumSpace = medium
        self.smallSpace = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.bigSpace == 0:
                return False
            self.bigSpace -=1
            return True
        elif carType == 2:
            if self.mediumSpace == 0:
                return False
            self.mediumSpace -=1
            return True
        else:
            if self.smallSpace == 0:
                return False
            self.smallSpace -=1
            return True
# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)