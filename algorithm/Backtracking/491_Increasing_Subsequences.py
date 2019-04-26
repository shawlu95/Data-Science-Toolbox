class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.subsets(nums, 0, [], res)
        return res

    def subsets(self, nums, start, temp, res):
        if len(temp) > 1:
            res.append(temp[:])

        used = {}
        for i in range(start, len(nums)):
            # similar to subset with duplicates, just skip element that's smaller than predexessor
            if len(temp) > 0 and temp[-1] > nums[i]:
                continue
            if nums[i] in used:
                continue
            used[nums[i]] = True

            # temp.append(nums[i])
            self.subsets(nums, i + 1, temp + [nums[i]], res)
            # temp.pop()

    def findSubsequences2(self, nums):
        arrs = []
        hash = {}
        res = []
        for n in nums:
            if n in hash:
                t, st = [], hash[n]
            else:
                t, st = [[n]], 0

            for arr in arrs[st:]:
                if n < arr[0][-1]:
                    continue
                for m in arr:
                    t.append(m + [n])
                    res.append(m + [n])
            arrs.append(t)
            hash[n] = len(arrs) - 1
        return res

arr = [4, 6, 7, 7]

solver = Solution()
ans = solver.findSubsequences2(arr)
print(ans)