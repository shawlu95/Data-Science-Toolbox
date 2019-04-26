class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.q = []
        while vec2d:
            vec = vec2d.pop(0)
            while vec:
                self.q.append(vec.pop(0))

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            return self.q.pop(0)

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.q) > 0

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())