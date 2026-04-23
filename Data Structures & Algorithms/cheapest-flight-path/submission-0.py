class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj = defaultdict(list)
        for u, v, cost in flights:
            adj[u].append((v, cost))

        h = [[0, src, 0]]  # cost, node, stops
        visited = dict()

        while h:
            c, n, s = heapq.heappop(h)

            if n == dst:
                return c

            if s > k or (n in visited and visited[n] <= s):
                continue
            visited[n] = s

            for n2, c2 in adj[n]:
                heapq.heappush(h, [c + c2, n2, s + 1])

        return -1