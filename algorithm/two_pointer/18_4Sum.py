class Solution:
    # combination of two fixed number, reducing the rest of the problem to 2-sum
    def fourSumPart1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        print(nums)
        N = 4
        ans = []
        def combo(nums, N, ans, path):
            if N == 2:
                ans.append(path)
                return
            for i in range(len(nums) - N + 1):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                combo(nums[i + 1:], N - 1, ans, path + [nums[i]])
        combo(nums, N, ans, [])
        print(ans)

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        print(nums)
        N = 4
        ans = []
        def combo(nums, N, ans, path, target):
            if N == 2:
                # solve two-sums
                l, r = 0, len(nums) - 1
                while l < r:
                    if nums[l] + nums[r] == target:
                        ans.append(path + [nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif nums[l] + nums[r] < target:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(len(nums) - N + 1):
                    # take advantages of sorted list (optional
                    if target < nums[i] * N or target > nums[-1] * N:
                        break

                    # avoid duplicate trees
                    if i > 0 and nums[i] == nums[i - 1]:
                        continue

                    # because array is sorted, only need to pick remaining element from [i+1:]
                    combo(nums[i + 1:], N - 1, ans, path + [nums[i]], target - nums[i])
        combo(nums, N, ans, [], target)
        return ans

solver = Solution()
solver.fourSum([1, 0, -1, 0, -2, 2], 0)