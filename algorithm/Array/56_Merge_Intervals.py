# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals: 'List[Interval]') -> 'List[Interval]':
        # corner case
        # 1. empty input
        # 2. one interval
        # 3. negative value

        buffer = []
        if not intervals:
            return buffer

        # sort start time ASC, so every nxt will start later than cur
        sorted_intervals = sorted(intervals, key=lambda x: x.start)

        # when processing next interval, two scenarios are possible
        # 1. disjoint, append current interval, hold next interval only
        # 2. overlap, join, hold one merged interval
        cur = sorted_intervals[0]
        for nxt in sorted_intervals[1:]:
            if cur.end < nxt.start: # mind equality sign
                buffer.append(cur)
                cur = nxt
            else:
                cur.end = max(cur.end, nxt.end)
        buffer.append(cur)
        return buffer
