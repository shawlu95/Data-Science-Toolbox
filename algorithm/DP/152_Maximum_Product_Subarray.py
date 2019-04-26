class Solution:
    # def maxProduct(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     for i in range(1, len(nums)):
    #         nums[i] = max(nums[i], nums[i] * nums[i - 1])
    #     return max(nums)

    def maxProduct3(self, nums):
        if not nums:
            return 0

        # locMin = nums[0]
        # locMax = nums[0]
        locMinPrev = nums[0]
        locMaxPrev = nums[0]
        gloMax = nums[0]

        for i in range(1, len(nums)):
            locMin = min(locMinPrev * nums[i], locMaxPrev * nums[i], nums[i])
            locMax = max(locMaxPrev * nums[i], locMinPrev * nums[i], nums[i])
            locMinPrev = locMin
            locMaxPrev = locMax
            gloMax = max(locMax, gloMax)
        return gloMax

    def maxProduct2(self, nums):
        ans = nums[0]

        # locMin, locMax stores the max/min product of subarray that ends with the current number
        locMin = locMax = ans
        for i in range(1, len(nums)):
            # multiplying with a negative number makes a negative number positive, a positive number negative
            if nums[i] < 0:
                locMax, locMin = locMin, locMax
            locMin = min(nums[i], locMin * nums[i])
            locMax = max(nums[i], locMax * nums[i])

            ans = max(ans, locMax)

        return ans

    def maxProduct(self, nums):
        ans = nums[0]

        # locMin, locMax stores the max/min product of subarray that ends with the current number
        locMin = locMax = ans
        for i in range(1, len(nums)):
            candidates = (nums[i], locMax * nums[i], locMin * nums[i])
            locMin = min(candidates)
            locMax = max(candidates)

            # warning: cannot do the following
            # locMin is updated before calculating locMax
            # locMin = min(nums[i], locMax * nums[i], locMin * nums[i])
            # locMax = max(nums[i], locMax * nums[i], locMin * nums[i])

            ans = max(ans, locMax)

        return ans


solver = Solution()
ans = solver.maxProduct3([-4,-3,-2])
print(ans)