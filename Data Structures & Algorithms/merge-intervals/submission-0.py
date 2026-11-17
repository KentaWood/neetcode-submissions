class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        res = []

        intervals.sort(key=lambda x: x[0])

        for i in range(1,len(intervals)):

            f,s = intervals[i - 1], intervals[i]

            # if f[1] > s[0]:
            #     one 
        
        return res

