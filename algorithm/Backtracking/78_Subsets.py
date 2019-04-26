class Solution:

    # O(n2^n)
    # Given a set of [distinct] integers, nums, return all possible subsets (the power set).
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        # nums.sort() not needed, only index matter
        def backtrack(nums, idx, ans, subset):
            ans.append(subset)
            for i in range(idx, len(nums)):
                backtrack(nums, i + 1, ans, subset + [nums[i]])
        backtrack(nums, 0, ans, [])
        return ans


class Solution2:
    def subsets(self, nums: 'List[int]') -> 'List[List[int]]':
        """
        []
        [1]
        [1,2]
        [1,2,3]
        [1,3]
        [2]
        [2,3]
        [3]

        edge case
        1. empty nums
        """
        buffer = []

        def trace(cur, tmp, e):
            buffer.append(list(tmp))

            # safe to ignore (implicit base case)
            # if cur == len(nums):
            #     return

            for nxt_idx in range(cur, len(nums)):
                nxt_num = nums[nxt_idx]
                # buffer.append(list(tmp)) ERROR!
                trace(nxt_idx + 1, tmp + [nxt_num], e + 1)  # making copy of tmp

        trace(0, [], 0)
        return buffer

solver = Solution2()
ans = solver.subsets([1, 2, 3])
# [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
print(ans)