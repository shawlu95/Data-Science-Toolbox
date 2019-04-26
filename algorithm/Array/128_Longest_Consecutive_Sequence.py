class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # sorting is not allowed
        s = set(nums)

        longest_streak = 0

        # this following two line ensures that we always start with the beginning of a streak
        # when it's not head of a streak, while loop is not entered, ensuring O(n) complexity
        for num in s:
            if num - 1 not in s:
                current_streak = 1
                while num + 1 in s:
                    current_streak += 1
                    num += 1
                longest_streak = max(longest_streak, current_streak)
        return longest_streak