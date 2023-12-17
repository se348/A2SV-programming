from sortedcontainers import SortedList
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.sorted_list = defaultdict(SortedList)      
        self.food_to_cuisine = {}
        self.food_to_rating = {}
        
        for i in range(len(foods)):
            self.sorted_list[cuisines[i]].add((-ratings[i], foods[i]))
            self.food_to_cuisine[foods[i]] = cuisines[i]
            self.food_to_rating[foods[i]] = ratings[i]
            
    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.food_to_cuisine[food]
        rating = self.food_to_rating[food]
        
        self.sorted_list[cuisine].remove((-rating, food))
        self.sorted_list[cuisine].add((-newRating, food))
        self.food_to_rating[food] = newRating
        
    def highestRated(self, cuisine: str) -> str:
        prev_rating, food =self.sorted_list[cuisine][0]
        return food


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)