# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """

        def incrementSlope(dic, slope):
            if slope not in dic:
                # when a slope is created, it immediately has two points on it
                dic[slope] = 1
            dic[slope] += 1

        l = len(points)
        m = 0
        for i in range(l):
            # the point itself if on a vertical line
            dic = {'i': 1}
            same = 0
            for j in range(i + 1, l):
                tx, ty = points[j].x, points[j].y
                if tx == points[i].x and ty == points[i].y:
                    same += 1
                elif points[i].x == tx:
                    slope = 'i'
                    incrementSlope(dic, slope)
                else:
                    slope = (points[i].y - ty) * 1.0 / (points[i].x - tx)
                    incrementSlope(dic, slope)
            m = max(m, max(dic.values()) + same)
        return m