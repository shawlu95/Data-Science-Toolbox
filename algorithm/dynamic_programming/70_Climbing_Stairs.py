class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = [0 for i in range(n + 1)]
        ans[0] = 1
        ans[1] = 1
        for i in range(2, len(ans)):
            ans[i] = ans[i - 1] + ans[i - 2]
        print(ans)
        return ans[-1]
