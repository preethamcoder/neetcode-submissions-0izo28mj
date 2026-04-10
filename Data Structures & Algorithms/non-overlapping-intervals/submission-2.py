class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        length = len(intervals)
        res = 0
        prev_end = intervals[0][1]
        for ind in range(1, length):
            if prev_end > intervals[ind][0]:
                res += 1
            else:
                prev_end = intervals[ind][1]
        return res