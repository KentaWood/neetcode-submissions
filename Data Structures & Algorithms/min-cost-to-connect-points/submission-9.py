class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        adj = defaultdict(list)

        for i in range(len(points)):
            x1, y1 = points[i]
            
            for j in range(i + 1,len(points)):
                x2,y2 = points[j]

                adj[i].append((j,abs(x1-x2) + abs(y1-y2)))
                adj[j].append((i,abs(x1-x2) + abs(y1-y2)))
        
        visited = [False] * len(points)

        # node, cost
        q = [(0,0)]
        heapq.heapify(q)

        res = 0

        while q:

            cost, node = heapq.heappop(q)

            if visited[node]:
                continue
            
            visited[node] = True

            res += cost

            for neigh, cost in adj[node]:

                if not visited[neigh]:
                    heapq.heappush(q,(cost,neigh))



        return res 