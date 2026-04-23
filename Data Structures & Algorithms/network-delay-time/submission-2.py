class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = defaultdict(list)

        # { node: [[target node, dist]]}
        for u, v, t in times:
            adj[u].append([v,t])
        
        h = [(0,k)]

        visited = set()
        res = 0
        
        while h:

            dist, node = heapq.heappop(h)

            if node in visited:
                continue
            
            visited.add(node)
            res = dist 

            for n2, d2 in adj[node]:
                if n2 not in visited:
                    heapq.heappush(h,[ dist + d2,n2])

        

        return res if len(visited) == n else -1 

        