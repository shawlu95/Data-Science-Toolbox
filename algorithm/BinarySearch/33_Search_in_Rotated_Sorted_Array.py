class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        return self.binarySearch(nums, target, 0, len(nums) - 1)

    def binarySearchRec(self, nums, target, i, j):
        if i > j:
            return -1
        m = (i + j) // 2
        if nums[m] == target:
            return m
        if nums[i] <= target < nums[m]:
            # left side is sorted and has target
            return self.binarySearch(nums, target, i, m - 1)
        elif nums[m] < target <= nums[j]:
            # right side is sorted and has target
            return self.binarySearch(nums, target, m + 1, j)
        elif nums[i] <= nums[m]:
            # right side is sorted and has no target
            return self.binarySearch(nums, target, m + 1, j)
        elif nums[m] <= nums[j]:
            # left side is sorted and has no target
            return self.binarySearch(nums, target, i, m - 1)

    def binarySearchIter(self, nums, target):
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] == target:
                return m
            elif nums[i] <= target < nums[m]:
                # left side is sorted and has target
                j = m - 1
            elif nums[m] < target <= nums[j]:
                # right side is sorted and has target
                i = m + 1
            elif nums[i] <= nums[m]:
                # right side is sorted and has no target
                i = m + 1
            elif nums[m] <= nums[j]:
                # left side is sorted and has no target
                j = m - 1
        return - 1

solver = Solution()
ans = solver.binarySearchIter([4,5,6,7,0,1,2], 0)
print(ans)