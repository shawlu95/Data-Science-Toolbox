class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.w = w
        self.n = len(w)
        self.s = sum(self.w)

        # cummulative sum
        for i in range(1, self.n):
            self.w[i] += self.w[i - 1]

    def pickIndex(self):
        """
        :rtype: int
        """
        seed = random.randint(1, self.s)
        l, r = 0, self.n - 1

        # see at which interval does seed lie
        while l < r:
            mid = (l + r) // 2
            if seed <= self.w[mid]:
                r = mid
            else:
                l = mid + 1
        return l

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()