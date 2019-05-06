class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if len(nums) == 1:
        #     return nums[0]

        # if nums[-1] > nums[0]:
        #     return nums[0]

        i, j = 0, len(nums) - 1
        while i < j:
            m = (i + j) // 2

            # pivot is on the right, and m cannot be pivot
            if nums[m] > nums[j]:
                i = m + 1
            elif nums[m] < nums[j]:
                # pivot is on the left, m may be pivot (do not increment)
                j = m
            else:
                # trick
                # test [1, 1], [3, 4, 2,2,2]
                j -= 1
        return nums[i]

solver = Solution()
ans = solver.findMin([3, 4, 2,2,2])
print(ans)