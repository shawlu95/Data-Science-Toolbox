class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
        # only difference from binary search
        # when target is smallest, l = 0 when terminated (r = -1)
        # when target is largest, l = len(nums) when terminated (r = len(nums) - 1)

        # ... a, b... target between a, b
        # if l == r == nums.index(b), then r -= 1, l == nums.index(b)
        # if l == r == nums.index(a), then l += 1, l == nums.index(a) + 1
        return l

solver = Solution()
solver.searchInsert([1, 2, 3, 5, 6], 4)
