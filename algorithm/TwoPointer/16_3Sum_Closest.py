class Solution:
    # directly modified from the two pointer approach in 3Sum
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ans = float('-inf')
        if len(nums) < 3:
            return

        nums.sort()
        for i in range(len(nums) - 2):
            # i has been incremented, check if it's equal to earlier i (i - 1)t
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]

                # optional: run faster
                # if s == target:
                #     return s

                if abs(s - target) < abs(ans - target):
                    ans = s

                if s < target:
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                else:
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return ans

solver = Solution()
ans = solver.threeSumClosest([-1, 2, 1, -4], 1)
print(ans)