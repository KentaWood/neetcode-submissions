class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        from collections import defaultdict
        import heapq

        adj = defaultdict(list)
        for s, t, c in times:
            adj[s].append((t, c))

        visited = [False] * (n + 1)  # using 1-based index
        h = [(0, k)]
        res = 0
        count = 0

        while h:
            cost, node = heapq.heappop(h)
            if visited[node]:
                continue
            visited[node] = True
            res = cost
            count += 1

            for neigh, costn in adj[node]:
                if not visited[neigh]:
                    heapq.heappush(h, (cost + costn, neigh))

        return res if count == n else -1
