class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        n = len(tasks)
        ans = []

        tasks = [[tasks[i][0], tasks[i][1], i] for i in range(n) ]
        tasks.sort()

        curr_time = 0
        i = 0
        schedule = []
        heapq.heapify([])

        while len(ans) < n:

            while i < n and tasks[i][0] <= curr_time:
                
                process, idx = tasks[i][1], tasks[i][2]
                heapq.heappush(schedule, [process,idx])

                i += 1

            if schedule:

                process, idx = heapq.heappop(schedule)
                curr_time += process

                ans.append(idx)

            else:
                
                curr_time = tasks[i][0]

            








        

        return ans