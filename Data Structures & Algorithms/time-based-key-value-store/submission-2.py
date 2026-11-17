class TimeMap:

    def __init__(self):
        self.mood = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mood[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.mood:
            return ""


        l, r = 0, len(self.mood[key]) 
        mood_ts = self.mood[key]

        while l < r:
            m = (l + r) // 2 
            print(m, l ,r,mood_ts[m][1])
            
            if mood_ts[m][0] <= timestamp:
                r = m - 1
            
            else:
                l = m + 1 
        
        return mood_ts[l][1]

             
        
