class UndergroundSystem:

    def __init__(self):
        self.adjacency_list = defaultdict(list)
        self.check_in_time = {}
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        
        self.check_in_time[id] = (stationName, t)
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        previous_station, loaded_time = self.check_in_time[id]
        self.check_in_time.pop(id)
        self.adjacency_list[(previous_station, stationName)].append(t - loaded_time)
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        count  = 0
        total = 0
        
        for neighbor in self.adjacency_list[(startStation, endStation)]:
            total += neighbor
            count += 1
        return (total / count)
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)