"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        sorted_intervals = [ (interval.start,interval.end) for interval in intervals]

        sorted_intervals.sort()
        print(sorted_intervals)

        

        for i in range(1,len(intervals)):

            prev_end = sorted_intervals[i - 1][1]
            curr_start = sorted_intervals[i][0]

            if prev_end > curr_start:
                return False


        return True
