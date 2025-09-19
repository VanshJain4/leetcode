import heapq
from collections import defaultdict
from typing import List

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_info = {}  # food -> [cuisine, rating]
        self.cuisine_heaps = defaultdict(list)  # cuisine -> heap of (-rating, food)

        for i in range(len(foods)):
            food = foods[i]
            cuisine = cuisines[i]
            rating = ratings[i]

            self.food_info[food] = [cuisine, rating]
            heapq.heappush(self.cuisine_heaps[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, _ = self.food_info[food]
        self.food_info[food][1] = newRating
        heapq.heappush(self.cuisine_heaps[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_heaps[cuisine]
        # lazy removal of outdated entries
        while heap:
            rating, food = heap[0]
            if -rating == self.food_info[food][1]:
                return food
            heapq.heappop(heap)
