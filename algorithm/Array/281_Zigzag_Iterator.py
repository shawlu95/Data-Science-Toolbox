class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.q = []
        # while v1 and v2:
        #     self.q.append(v1.pop(0))
        #     self.q.append(v2.pop(0))
        # v = v1
        # if v2:
        #     v = v2
        # while v:
        #     self.q.append(v.pop(0))

        vs = [v1, v2]
        k = len(vs)
        while any(vs):
            for i in range(k):
                v = vs[i]
                if v:
                    self.q.append(v.pop(0))

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

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())