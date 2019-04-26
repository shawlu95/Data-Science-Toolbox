class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1

        # possible anser is between [1, k + 1]
        # k is largest number
        l = [0] * (max(nums) + 1)

        # save num at index num - 1
        for num in nums:
            if num > 0:
                l[num - 1] = -num
        for i in range(len(l)):
            if l[i] == 0:
                return i + 1
