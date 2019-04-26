class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def binarySearch(target, nums):
            """
            return type: int (ceiling of the insert position)
            if target is greater than all nums, return len(nums)
            """
            if not nums:
                return 0

            l = 0
            r = len(nums) - 1

            while l <= r:
                m =  (l + r) // 2
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return l

        res = [] # not the longest increasing subsequence, but the same length

        for num in nums:
            pos = binarySearch(num, res)
            if pos >= len(res):
                res.append(num)
            else:
                res[pos] = num
        print(res)
        return len(res)

solver = Solution()
# ans = solver.lengthOfLIS([3, 4, 7, 6, 2])
# ans = solver.lengthOfLIS([10,9,2,5,3,7,101,18])
ans = solver.lengthOfLIS([3,5,6,2,5,4,19,5,6,7,12])
print(ans)
