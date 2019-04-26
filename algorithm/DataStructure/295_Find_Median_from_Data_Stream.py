from heapq import *
class MedianFinder:
    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num):
        if len(self.small) == len(self.large):
            # add new elem to small heap (max heap)
            # take largest element from small heap, add to large heap
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            # large heap has size N/2 + 1, becomes N/2 + 2
            # move smallest element to max heap, both heaps are now N/2 + 1
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])