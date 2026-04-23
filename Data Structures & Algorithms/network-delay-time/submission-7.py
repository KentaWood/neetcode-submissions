class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = defaultdict(list)

        # adj list source --> (dest, cost)
        for s,d,c in times:
            adj[s].append((d,c))
        
        # (path cost, dest)
        h = [(0,k)]
        visited = [False] * (n + 1) # 1 - index
        visits = 0
        res = 0
        print(adj)

        while h:

            cost, node = heapq.heappop(h)

            if visited[node]:
                continue
            


            res = cost
            visited[node] = True
            # print(node)
            visits += 1

            for nei, cost2 in adj[node]:
                print(node, nei)
                if not visited[nei]:
                    heapq.heappush(h,(cost + cost2, nei))

        print(visits, n)        
        return res if visits == n else -1

            
            



