class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """

    def findPosition(self, nums, target):
        # write your code here
        l, h = 0, len(nums) - 1
        def rec(nums, l, h, t):
            if h < l: # do not break when l == h
                return -1
            m = (l + h) // 2
            mid_num = nums[m]

            if mid_num == t:
                return m
            elif mid_num > t:
                # don't forget to return the result from later call stack
                return rec(nums, l, m - 1, t)
            else:
                # don't forget to return the result from later call stack
                return rec(nums, m + 1, h, t)
        return rec(nums, l, h, target)

solver = Solution()
print(solver.findPosition([1, 2, 2, 4, 5, 5], 2))
