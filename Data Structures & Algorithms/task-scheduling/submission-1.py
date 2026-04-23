from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        counts = Counter(tasks)
        t = 0

        mh = [(-freq,task) for task,freq in counts.items()]
        heapq.heapify(mh)

        q = deque()

        while q or mh:

            t += 1

            if mh:
                count, task = heapq.heappop(mh)

                count += 1

                if count != 0:
                    q.append((t + n, count, task))

            if q and q[0][0] == t:
                time, freq, task = q.popleft()
                heapq.heappush(mh,(freq,task))


        

        return t
        