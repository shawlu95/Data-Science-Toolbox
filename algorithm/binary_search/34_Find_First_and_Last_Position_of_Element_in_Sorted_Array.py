class Solution(object):
    def searchLeftMost(self, nums, target):
        # init with len, instead of len - 1, to handle corner case or one-element array
        l, r = 0, len(nums)
        while l != r:
            m = (l + r) // 2
            if nums[m] >= target:
                r = m
            else:
                l = m + 1
        return l

    def searchRightMost(self, nums, target):
        # init with len, instead of len - 1, to handle corner case or one-element array
        l, r = 0, len(nums)
        while l != r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m
            else:
                l = m + 1
        return r - 1

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return True
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return False

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if self.search(nums, target):
            return [self.searchLeftMost(nums, target), self.searchRightMost(nums, target)]
        return [-1, -1]

solver = Solution()
# print(solver.searchLeftMost([1, 2, 5, 5, 5, 9], 5))
# print(solver.searchLeftMost([1, 2, 3, 3, 3, 5, 5, 5, 9], 5))
# print(solver.searchLeftMost([1, 2, 5, 5, 5, 7, 7, 7, 9], 5))
#
# print(solver.searchRightMost([1, 2, 5, 5, 5, 9], 5))
# print(solver.searchRightMost([1, 2, 3, 3, 3, 5, 5, 5, 9], 5))
print(solver.searchRightMost([1, 2, 5, 5, 5, 7, 7, 7, 9], 5))

# print(solver.searchLeftMost([5,7,7,8,8,10], 8))
# print(solver.searchRightMost([5,7,7,8,8,10], 8))
#
# print(solver.searchRange([1, 2, 3, 3, 3, 5, 5, 5, 9], 5))