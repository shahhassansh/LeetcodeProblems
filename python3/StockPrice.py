class StockPrice:

    def __init__(self):
        self.current_time = 0
        self.price_time = SortedSet()
        self.time_to_price = {}

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.time_to_price:
            self.price_time.remove((self.time_to_price[timestamp], timestamp))
        
        self.time_to_price[timestamp] = price
        self.price_time.add((price, timestamp))
        self.current_time = max(self.current_time, timestamp)
        

    def current(self) -> int:
        return self.time_to_price[self.current_time]
        

    def maximum(self) -> int:
        return self.price_time[-1][0]

        

    def minimum(self) -> int:
        return self.price_time[0][0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
