class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        count = {0 : 1}
        rolling = 0
        for num in nums:
            rolling += num
            if rolling - k in count:
                ans += count[rolling - k]

            count[rolling] = count.get(rolling, 0) + 1
            print(ans, num, rolling, count)
        return ans

solver = Solution()
solver.subarraySum([3, 4, 7, 7, -7, -3, 1, 4, 2], 7)