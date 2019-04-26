class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        for i in range(2, len(cost)):
            cost[i] += min(cost[i - 1], cost[i - 2])
        return min(cost[-1], cost[-2])

    def minCostClimbingStairs2(self, cost):

        dp = [0] * (len(cost))
        dp[0], dp[1] = cost[0], cost[1]

        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 2] + cost[i], dp[i - 1] + cost[i])
        print(dp)
        return min(dp[-2], dp[-1])


solver = Solution()
ans = solver.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
print(ans)