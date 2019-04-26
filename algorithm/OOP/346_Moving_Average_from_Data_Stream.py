class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.arr = []

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.arr.append(val)

        if len(self.arr) < self.size:
            return sum(self.arr) / len(self.arr)

        return sum(self.arr[-self.size:]) / self.size

# Your MovingAverage object will be instantiated and called as such:
obj = MovingAverage(3)
print(obj.next(1))
print(obj.next(10))
print(obj.next(3))
print(obj.next(5))


