class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        prices = [float("inf")] * n
        prices[src] = 0

        adj = defaultdict(list)

        for s, d, c in flights:
            adj[s].append([d,c])

        # cost, node, stops
        bfs = deque([[0,src,0]]) 

        while bfs:
            
            cost, node, stops = bfs.popleft()

            if stops > k:
                continue
            
            if node == dst:
                cheapest = min(cheapest, cost)
                continue
            
            for neigh, cost2 in adj[node]:
                
                if prices[node] > cost + cost2:
                    prices[node] = cost + cost2
                    bfs.append([cost + cost2, neigh, stops + 1])
        

        return prices[dst] if prices[dct] != float('inf') else -1





        


        