class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        length = len(intervals)
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for each in range(1, length):
            curr_start = intervals[each][0]
            prev_end = res[-1][1]
            curr_end = intervals[each][1]
            if curr_start <= prev_end:
                res[-1][-1] = max(prev_end, curr_end)
            else:
                res.append([curr_start, curr_end])
        return res