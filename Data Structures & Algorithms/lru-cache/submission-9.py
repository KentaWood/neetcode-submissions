class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = []
        self.map = {}
        

    def get(self, key: int) -> int:
        if self.queue and (key in self.map):
            self.queue.remove(key)
            self.queue.append(key)
            return self.map[key]
        else: 
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map[key] = value
            self.queue.remove(key)
            self.queue.append(key)
            
        else :
            if len(self.queue) == self.capacity:
                lru_key = self.queue.pop(0)
                del self.map[lru_key]
                
                self.queue.append(key)
                self.map[key] = value
            else:
                self.queue.append(key)
                self.map[key] = value