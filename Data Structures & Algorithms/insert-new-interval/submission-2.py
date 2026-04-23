class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        p, n = 0, len(intervals)

        # no merging 
        while p < n and newInterval[0] > intervals[p][1]:
            res.append(intervals[p])
            p += 1


        # merging 
        while p < n and newInterval[1] >= intervals[p][0]:
            newInterval[0] = min(newInterval[0],intervals[p][0])
            newInterval[1] = max(newInterval[1],intervals[p][1])
            p += 1

        res.append(newInterval)

        return res + intervals[p:]

        