class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        prevCount = 1
        res = 0
        i = 0

        def advance(i, count):
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                count += 1
                i += 1
            return i, count

        while i < len(nums):
            count = 1
            if i > 0 and nums[i] - nums[i - 1] == 1:
                i, count = advance(i, count)
                res = max(res, count + prevCount)
            else:
                i, count = advance(i, count)
            prevCount = count
            i += 1

        return res

    def findLHSHash(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        ans = 0
        for num in count:
            if num + 1 in count:
                ans = max(ans, count[num] + count[num + 1])
        return ans

    def findLHSHash2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        ans = 0
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if num + 1 in count:
                ans = max(ans, count[num] + count[num + 1])
            if num - 1 in count:
                ans = max(ans, count[num] + count[num - 1])
        return ans


arr = [1,3,2,2,5,2,3,7]
solver = Solution()
ans = solver.findLHS(arr)
print(ans)