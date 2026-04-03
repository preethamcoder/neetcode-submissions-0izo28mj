"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key= lambda x: x.start)
        length = len(intervals)
        for ind in range(1, length):
            prev_end = intervals[ind-1].end
            curr_start = intervals[ind].start
            if curr_start < prev_end:
                return False
        return True