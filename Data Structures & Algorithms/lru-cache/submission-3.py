class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.queue = []

    def get(self, key: int) -> int:
        if key in self.cache:
            # Move the accessed key to the end to show that it was recently used
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Move the existing key to the end to show that it was recently used
            self.queue.remove(key)
        elif len(self.cache) >= self.capacity:
            # Remove the least recently used item
            lru_key = self.queue.pop(0)
            del self.cache[lru_key]
        
        # Add the new key-value pair
        self.cache[key] = value
        self.queue.append(key)