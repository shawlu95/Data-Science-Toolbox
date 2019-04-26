# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # Collect the intervals strictly left or right of the new interval,
    # then merge the new one with the middle ones (if any) before
    #inserting it between left and right ones.
    def insert(self, intervals, newInterval):
        s, e = newInterval.start, newInterval.end
        left = [i for i in intervals if i.end < s]
        right = [i for i in intervals if i.start > e]
        if left + right != intervals:
            s = min(s, intervals[len(left)].start)
            e = max(e, intervals[-(len(right) + 1)].end)
            # or intervals[~len(right)]
        return left + [Interval(s, e)] + right