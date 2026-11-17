class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = defaultdict(list)

        # start, dest, cost
        for s ,d, c in times:
            adj[s].append((d,c))
        
        # node, cost of current path
        q = [(0,k)]

        visited = [False] * (n + 1) # 1-index
        visited[0] = True
        res = 0 

        while q:
            print(q)
            cost1, node = heapq.heappop(q)


            if visited[node]:
                continue

            visited[node] = True

            res += cost1

            for neigh,cost2 in adj[node]:

                if not visited[neigh]:
                    heapq.heappush(q, (cost2, neigh))

        return res if visited else -1 




        
        