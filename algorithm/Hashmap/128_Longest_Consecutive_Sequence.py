class Solution(object):
    def longestConsecutive1(self, nums):
        if not nums:
            return 0

        nums.sort()

        longest_streak = 1
        current_streak = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    current_streak += 1
                else:
                    longest_streak = max(longest_streak, current_streak)
                    current_streak = 1

        return max(longest_streak, current_streak)

    def longestConsecutive2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)

        longest_streak = 0

        for num in s:
            if num - 1 not in s:
                current_streak = 1
                while num + 1 in s:
                    current_streak += 1
                    num += 1
                longest_streak = max(longest_streak, current_streak)
        return longest_streak

