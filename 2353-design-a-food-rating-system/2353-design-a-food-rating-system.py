from sortedcontainers import SortedList
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisines = defaultdict(list) 
        self.food_rating_map = {}
        self.food_cuisine_map = {}
        
        for i in range(len(foods)):
            self.food_rating_map[foods[i]] = ratings[i]
            self.food_cuisine_map[foods[i]] = cuisines[i]
            
            heappush(self.cuisines[cuisines[i]], (-ratings[i], foods[i]))
            
        
        
    def changeRating(self, food: str, newRating: int) -> None:
        self.food_rating_map[food] = newRating
        cuisine = self.food_cuisine_map[food]
        
        heappush(self.cuisines[cuisine], (-newRating, food))
        
        
    def highestRated(self, cuisine: str) -> str:
        the_heap = self.cuisines[cuisine]
        while self.food_rating_map[the_heap[0][1]] != -the_heap[0][0]:
            heappop(the_heap)
        
        return the_heap[0][1]

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)