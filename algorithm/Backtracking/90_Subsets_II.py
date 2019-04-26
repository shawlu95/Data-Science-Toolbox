class Solution:

    #  Given a collection of integers that [might contain duplicates], nums, return all possible subsets (the power set).
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        array may contain duplicate elements
        duplciate elements can appear in subset
        order matters does not matter, [1, 2] is same as [2, 1]
        """
        ans = []
        nums.sort()

        # implicit base case
        def backtrack(nums, idx, ans, subset):
            # simple fix, check if subset exists
            # if subset not in ans:
            #     ans.append(subset)
            ans.append(subset)
            for i in range(idx, len(nums)):
                # clever fix, check if consecutive numbers are identical, if so start with the last one
                # without i > idx: [[], [1], [1, 2], [2]] discarded subset whose last element is same as first element appended! Not good
                # with i > idx: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                backtrack(nums, i + 1, ans, subset + [nums[i]])
        backtrack(nums, 0, ans, [])
        return ans

    def subsetsWithDup2(self, nums: 'List[int]') -> 'List[List[int]]':

        """
        when tracking index

        1-1
        2-12
        3-122
        2-12'
        1-2
        2-22
        1-2'

        if nums[i] == nums[i+1]
        nums[i] will form subset with all elements following [i+1:]
        nums[i+1] will form subset with all elements following [i+2:]
        tree from num[i] contain tree from nums[i+1]
        """
        nums.sort()
        buffer = []

        def trace(cur, tmp):
            buffer.append(list(tmp))

            for nxt_idx in range(cur, len(nums)):
                nxt_num = nums[nxt_idx]
                # needs to be bigger than cur, if cur is same as next
                # next needs to be appended to tmp e.g. [1, 2, 2]
                # without first condition check, no duplicate number
                # can exist in tmp
                if nxt_idx > cur and nxt_num == nums[nxt_idx - 1]:
                    continue
                trace(nxt_idx + 1, tmp + [nxt_num])

        trace(0, [])
        return buffer

    # ad hoc
    def subsetsWithDup3(self, nums):
        if not nums:
            return []
        nums.sort()
        res, cur = [[]], []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                cur = [item + [nums[i]] for item in cur]
            else:
                cur = [item + [nums[i]] for item in res]
            res += cur
        return res

solver = Solution()
ans = solver.subsetsWithDup2([1,2,2])
# [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
print(ans)