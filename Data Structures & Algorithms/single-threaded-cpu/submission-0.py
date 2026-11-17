class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        n = len(tasks)
        
        tasks = [[tasks[i][0], tasks[i][1], i] for i in range(n) ]

        print(tasks)

        