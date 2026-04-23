class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = defaultdict(list)

        # start, dest, cost
        for s ,d, c in times:
            adj[s].append((d,c))
        
        # node, cost of current path
        q = [(0,k)]
        heapq.heapify(q)

        # visited = [False] * (n + 1) # 1-index
        # visited[0] = True

        visited = set()
        res = 0 

        while q:
            # print(q)
            cost1, node = heapq.heappop(q)


            if node in visited:
                continue

            visited.add(node) 

            res = cost1

            for neigh,cost2 in adj[node]:

                if neigh not in visited:
                    heapq.heappush(q, (cost2 + cost1, neigh))
        
        return res if len(visited) == n else -1 




        
        