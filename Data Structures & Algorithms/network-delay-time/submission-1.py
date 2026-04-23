class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = defaultdict(list)
        nodes_reached = 0
        # min_dist = 0 

        for u,v,w in times:
            adj[u].append((v,w))

        # i + 1 is the nod, distances[i + 1 ] is the distance from node k  
        distances = [float('inf') for x in range(n)]
        distances[k - 1] = 0

        visited = set()
        q = [(0, k)]
        
        while q:

            curr_dist, node = heapq.heappop(q)

            if node in visited:
                continue 
            
            visited.add(node)
            
            for v,w in adj[node]:

                dist = curr_dist + w

                if distances[v - 1] > dist:
                    distances[v - 1] = dist
                    heapq.heappush(q,(dist,v))
            
            


        
        return max(distances) if len(visited) == n else -1 

        