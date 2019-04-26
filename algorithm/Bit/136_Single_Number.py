class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # a ^ 0 == a
        # a ^ a == 0
        # a ^ b ^ a = a ^ a ^ b = 0 ^ b = b
        a = 0
        for i in nums:
            a ^= i
            print(a)
        return a


print(15 ^ 10)
print(10 ^ 15)

solver = Solution()
solver.singleNumber([4,1,2,1,2])