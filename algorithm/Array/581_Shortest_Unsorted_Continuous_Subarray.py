class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_sorted = sorted(nums)
        for i, n in enumerate(nums):
            if n != nums_sorted[i]:
                break

        if i == len(nums) - 1:
            return 0

        for j in range(len(nums) - 1, -1, -1):
            if nums[j] != nums_sorted[j]:
                break

        return j - i + 1