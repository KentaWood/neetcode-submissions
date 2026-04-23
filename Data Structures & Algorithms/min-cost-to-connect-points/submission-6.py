class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        

        adj = defaultdict(list)

        for i in range(len(points)):
            for j in range(i, len(points)):
                x1,y1 = points[i]
                x2,y2 = points[j]

                adj[i].append((j,abs(x1 - x2) + abs(y1 - y2)))
                adj[j].append((i, abs(x1 - x2) + abs(y1 - y2)))

        # node start from the node 0 [cost,node]
        h = [[0,0]]

        visited = [False] * len(points) # 0-index based
        res = 0
        while h:

            cost,node = heapq.heappop(h)

            
            if visited[node]:
                continue
            
            res += cost
            visited[node] = True

            # print(cost,node)
            for nei, cost2 in adj[node]:

                # print(nei,cost2)

                if not visited[nei]:
                    heapq.heappush(h,(cost2, nei))

             

        return  res
            


        

