class TimeMap:

    def __init__(self):
        self.mood = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mood[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:

        moods = self.mood[key] 

        if not moods or moods[0][0] > timestamp:
            return ""

        l, r = 0, len(moods) - 1

        while l <= r:

            m = (r - l) // 2 + l

            if moods[m][0] <= timestamp:
                res = moods[m][1]
                l = m + 1
            else:
                r = m - 1

        return res
                




        
