class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right, count = {}, {}, {}

        for idx, num in enumerate(nums):
            # if num key exists
            if num not in left:
                left[num] = idx
            right[num] = idx
            count[num] = count.get(num, 0) + 1

        ans = len(nums)

        degree = max(count.values())

        # iterate over keys
        for num in count:
            if count[num] == degree:
                ans = min(ans, right[num] - left[num] + 1)

        return ans

solver = Solution()
solver.findShortestSubArray([1,2,2,3,1,4,2])