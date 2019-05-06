import heapq
class KthLargest(object):

    def __init__(self, k, nums):
        self.pool = nums
        self.k = k
        heapq.heapify(self.pool)
        while len(self.pool) > k:
            heapq.heappop(self.pool)

    def add(self, val):
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        elif val > self.pool[0]:
            # pop heap top (kth largest)
            # add new val (may not be top)
            heapq.heappop(self.pool)
            heapq.heappush(self.pool, val)
            # heapq.heapreplace(self.pool, val)
        return self.pool[0]

class KthLargest2(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.nums = sorted(nums)
        self.k = k

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        for i in range(len(self.nums), 0, -1):
            if val >= self.nums[i - 1]:
                self.nums.insert(i, val)
                break
        if len(self.nums) == 0 or i == 1:
            self.nums.insert(0, val)
        if self.k <= len(self.nums):
            return self.nums[-self.k]
        return self.nums[-1]

# Your KthLargest object will be instantiated and called as such:
k = 3
nums = [4,5,8,2]
obj = KthLargest(k, nums)

obj.add(3)
obj.add(5)
obj.add(10)
obj.add(9)
obj.add(4)
