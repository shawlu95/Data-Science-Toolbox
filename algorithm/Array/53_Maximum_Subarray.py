class Solution(object):
    def maxSubArray(self, nums):
        """
        :type height: List[int]
        :rtype: int
        """
        if not nums:
            return
        maxSum = - float('inf')
        cumSum = 0
        for num in nums:
            cumSum = max(num, cumSum + num)
            maxSum = max(cumSum, maxSum)
        return maxSum

    def maxSubArrayDP(self, nums):
        if not nums:
            return
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i - 1])
        return max(nums)


solver = Solution()
ans = solver.maxSubArrayDP([-2,1,-3,4,-1,2,1,-5,4])
print(ans)