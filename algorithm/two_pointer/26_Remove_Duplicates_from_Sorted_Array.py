class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s, f = 0, 1
        while f < len(nums):
            if nums[s] != nums[f]:
                s += 1
                nums[s] = nums[f]
            f += 1

        return nums, s + 1

solver = Solution()
# ans = solver.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
ans = solver.removeDuplicates([1, 2, 3])
print(ans)