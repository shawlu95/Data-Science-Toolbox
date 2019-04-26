class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []

        def backtrack(nums, subset, ans):
            if len(subset) == len(nums):
                ans.append(subset)
                return
            for i in range(len(nums)):
                # cannot reuse same element
                # input does not contain duplicates, but the same number cannot appear twice
                if nums[i] in subset:
                    continue
                backtrack(nums, subset + [nums[i]], ans)
        backtrack(nums, [], ans)
        return ans

solver = Solution()
ans = solver.permute([1,2,3])
print(ans)