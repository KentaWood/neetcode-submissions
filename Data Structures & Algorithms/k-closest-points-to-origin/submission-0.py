class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        

        h = []


        for x, y in points:

            heapq.heappush(h, (math.sqrt(x ** 2 + y ** 2), [x,y]))

        print(h)
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(h)[1])


        return res