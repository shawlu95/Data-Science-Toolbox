class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        s = 0
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i - 1]
            s += max(diff, 0)
        return s


solver = Solution()
ans = solver.maxProfit([1,2,3,4,5])
print(ans)