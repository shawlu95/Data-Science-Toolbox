class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def binarySearch(target, nums):
            """
            return type: int (ceiling of the insert position)
            """
            if not nums:
                return 0

            l = len(nums)
            start = 0
            end = l - 1

            while start <= end:
                half = start + (end - start) // 2
                if nums[half] == target:
                    return half
                elif nums[half] < target:
                    start = half + 1
                else:
                    end = half - 1

            return start

        if not nums:
            return 0
        l = len(nums)
        res = []

        for num in nums:
            pos = binarySearch(num, res)
            if pos >= len(res):
                res.append(num)
            else:
                res[pos] = num
        return len(res)
