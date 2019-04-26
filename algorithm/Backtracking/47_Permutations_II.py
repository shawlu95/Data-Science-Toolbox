# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        # keep track of index, not actual element itself, which may be duplicates
        used = [False] * len(nums)
        def backtrack(nums, subset, ans, used):
            if len(subset) == len(nums) and subset not in ans:
                ans.append(subset)
                return

            for i in range(len(nums)):
                if used[i] is True:
                    continue
                used[i] = True
                backtrack(nums, subset + [nums[i]], ans, used)
                used[i] = False

        backtrack(nums, [], ans, used)
        return ans

    # recursion using dictonary to keep track of used elements in CURRENT recursive stack
    def permuteUnique2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        res = []

        def helper(res, nums, path):
            if not nums:
                res.append(path)
                return

            # dic is used for accounting for current stack only, if a number has been used, it cannot be used again
            # in current stack
            dic = {x: 1 for x in nums}

            for i in range(len(nums)):
                if dic[nums[i]] == 1:
                    # permute a truncated array excluding current element
                    helper(res, nums[:i] + nums[i + 1:], path + [nums[i]])
                    dic[nums[i]] -= 1

        helper(res, nums, [])
        return res

    # recursion using hashset to keep track of used elements in CURRENT recursive stack
    def permuteUnique3(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        res = []

        def helper(res, nums, path):
            if not nums:
                res.append(path)
                return

            # s is used for accounting current stack only, if a number has been used, it cannot be used again
            # in current stack, whether the number is the same or different index as the one already used
            s = set()

            for i in range(len(nums)):
                if nums[i] not in s:
                    # permute a truncated array excluding current element
                    helper(res, nums[:i] + nums[i + 1:], path + [nums[i]])
                    s.add(nums[i])

        helper(res, nums, [])
        return res

    # impossible solution for study
    def permuteUnique4(self, num):
        if not num:
            return []

        def permute(num):
            if len(num) == 1:
                return [num]

            ret = []
            for index, elt in enumerate(num):
                if index > 0 and num[index - 1] == elt:
                    continue
                ret += [[elt] + p for p in permute(num[:index] + num[index + 1:])]
            return ret

        return permute(sorted(num))






solver = Solution()
ans = solver.permuteUnique3([0, 1, 1, 2])
print(ans)