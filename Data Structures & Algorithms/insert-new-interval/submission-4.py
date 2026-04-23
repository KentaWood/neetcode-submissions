class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        p, n = 0, len(intervals)

        # no merging
        while p < n and intervals[p][1] < newInterval[0]:
            res.append(intervals[p])
            p += 1
        
        # merging occurs
        while p < n and intervals[p][0] <= newInterval[1]:
            
            newInterval[0]  = min(intervals[p][0],newInterval[0])
            newInterval[1] = max(intervals[p][1],newInterval[1])
            p += 1 

        res.append([newInterval[0],newInterval[1]])

        # no merging
        while p < n:
            res.append(intervals[p])
            p += 1
    
        return res 
