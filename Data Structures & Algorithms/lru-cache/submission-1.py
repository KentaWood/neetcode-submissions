class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = []
        self.map = {} 
        self.count = 0
        

    def get(self, key: int) -> int:
        
        return self.map[key] if key in self.map else -1
        
        
        

    def put(self, key: int, value: int) -> None:
        if self.count == self.capacity:
            del self.map[self.queue.pop(0)]
            self.map[key] = value
            self.queue.append(key)
        else:
            self.map[key] = value
            self.queue.append(key)
            self.count += 1
        print(self.map)
        
        
        
        

            
            
        
        