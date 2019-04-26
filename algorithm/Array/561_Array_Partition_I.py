class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum([nums[i] for i in range(0, len(nums), 2)])

    # def arrayPairSumHash(self, nums):
    #     arr = [0] * 20001
    #     lim = 10000
    #     for num in nums:
    #         arr[num + lim] += 1
    #
    #     d, s = 0, 0
    #     for i in range(-10000, 10001):
    #         s += (arr[i + lim] + 1 - d) / 2 * i
    #         d = (2 + arr[i + lim] - d) % 2
    #     return s


solver = Solution()
ans = solver.arrayPairSumHash([1,4,3,2])
print(ans)