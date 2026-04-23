class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        adj = defaultdict(list)
        N = len(points)

        for i in range(N):
            x1,y1 = points[i]
            for j in range(i+1, N):
                x2,y2 = points[j]

                dist = abs(x1 - x2)  + abs(y1 - y2)
                
                adj[i].append([j,dist])
                adj[j].append([i,dist])

        visited = set()
        res = 0
        h = [[0,0]] 

        while h:
            cost, node = heapq.heappop(h)

            if node in visited:
                continue
            
            res += cost
            visited.add(node)

            for neigh, ncost in adj[node]:
                if neigh not in visited:
                    heapq.heappush(h,[ncost,neigh])
        
        return res




        