class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = []
        self.map = {}

    def get(self, key: int) -> int:
        if key in self.map:
            # Move the accessed key to the end (most recently used)
            self.queue.remove(key)
            self.queue.append(key)
            return self.map[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            # Update the value and move the key to the end (most recently used)
            self.map[key] = value
            self.queue.remove(key)
            self.queue.append(key)
        else:
            if len(self.queue) == self.capacity:
                # Remove the least recently used key
                lru_key = self.queue.pop(0)
                del self.map[lru_key]
            # Add the new key-value pair
            self.queue.append(key)
            self.map[key] = value