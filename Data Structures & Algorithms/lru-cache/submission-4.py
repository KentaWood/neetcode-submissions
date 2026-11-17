class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = []
        self.map = {}
        

    def get(self, key: int) -> int:
        if self.queue and (key in self.map):
            return self.map[key]
        else: 
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map[key] = value
            
        if len(self.queue) == self.capacity:
            print(self.queue)
            del self.map[self.queue.pop(0)]
            
            self.queue.append(key)
            self.map[key] = value
            print(self.queue)
        else:
            self.queue.append(key)
            self.map[key] = value