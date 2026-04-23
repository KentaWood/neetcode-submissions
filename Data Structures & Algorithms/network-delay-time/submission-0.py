import heapq
from collections import defaultdict
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = defaultdict(list)

        for u, v, w in times:  # fixed variable naming
            adj[u].append((v, w))

        distances = [float('inf')] * n
        distances[k - 1] = 0  # fix indexing for 1-based node k

        visited = set()
        q = [(0, k)]

        while q:
            curr_dist, node = heapq.heappop(q)

            if node in visited:
                continue

            visited.add(node)

            for neighbor, weight in adj[node]:
                dist = curr_dist + weight
                if distances[neighbor - 1] > dist:
                    distances[neighbor - 1] = dist
                    heapq.heappush(q, (dist, neighbor))

        return max(distances) if len(visited) == n else -1
