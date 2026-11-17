class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = defaultdict(list)

        for s, t, c in times:
            adj[s].append((t,c))

        visited = [False] * n
        res = 0
        h = [[0,k]]

        while h:
            cost, node = heapq.heappop(h)

            if visited[node]:
                continue
            
            visited[node] = True
            res = cost

            for neigh, costn in adj[node]:

                if not visited[neigh]:
                    heapq.heappush(h, (cost + costn, neigh)) 
        return res if len(visited) == n else -1  


        