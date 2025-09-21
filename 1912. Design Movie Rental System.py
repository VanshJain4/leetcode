from sortedcontainers import SortedList

class MovieRentingSystem:
    def __init__(self, n, entries):
        self.available = defaultdict(SortedList)  # movie -> SortedList[(price, shop)]
        self.rented = SortedList()  # SortedList[(price, shop, movie)]
        self.price_map = {}
        for shop, movie, price in entries:
            self.available[movie].add((price, shop))
            self.price_map[(shop, movie)] = price

    def search(self, movie):
        # Return up to 5 cheapest available shops for the movie
        return [shop for price, shop in self.available[movie][:5]]

    def rent(self, shop, movie):
        price = self.price_map[(shop, movie)]
        self.available[movie].remove((price, shop))
        self.rented.add((price, shop, movie))

    def drop(self, shop, movie):
        price = self.price_map[(shop, movie)]
        self.rented.remove((price, shop, movie))
        self.available[movie].add((price, shop))

    def report(self):
        # Return up to 5 cheapest rented movies
        return [[shop, movie] for price, shop, movie in self.rented[:5]]
