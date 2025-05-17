class LRUCache:

    def __init__(self, capacity: int):
        self.LRU_Cache = {}
        self.stack = []
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if key not in self.stack:
            return -1
        if key in self.stack:
            self.stack.remove(key)
        if len(self.stack) < self.capacity:
            self.stack.append(key)
        else:
            self.stack.pop(0)
            self.stack.append(key)
        return self.LRU_Cache[key]
        

    def put(self, key: int, value: int) -> None:
        self.LRU_Cache[key] = value
        if key in self.stack:
            self.stack.remove(key)
        if len(self.stack) < self.capacity:
            self.stack.append(key)
        else:
            self.stack.pop(0)
            self.stack.append(key)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
