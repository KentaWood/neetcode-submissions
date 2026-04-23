class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        

        N = len(points)
        adj = {i: [] for i in range(N)}
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        res = 0
        visit = [False] * N
        visits = 0 
        minH = [[0, 0]]

        while visits < N:

            c1,n1 = heapq.heappop(minH)

            if visit[n1]:
                continue
            
            visit[n1] = True
            visits += 1
            res += c1

            for c2, n2 in adj[n1]:

                if not visit[n2]:
                    heapq.heappush(minH,[c2, n2])

        return res


            


        

