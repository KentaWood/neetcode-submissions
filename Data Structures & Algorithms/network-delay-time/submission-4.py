class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = defaultdict(list)

        for s, t, c in times:
            adj[s].append((t,c))

        visited = set()
        res = 0
        h = [[0,k]]

        while h:
            cost, node = heapq.heappop(h)

            if node in visited:
                continue
            
            visited.add(node)
            res = cost

            for neigh, costn in adj[node]:

                if neigh not in visited:
                    heapq.heappush(h, (cost + costn, neigh)) 
        return res if len(visited) == n else -1  


        