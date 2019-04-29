class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        s1, s2 = 0, nums[0]
        for num in nums[1:]:
            s1, s2 = s2, max(s1 + num, s2)
        return s2

# simplify edge case to be handled implicitly

class Solution:
    def rob(self, nums: List[int]) -> int:
        s1, s2 = 0, 0
        for num in nums:
            s1, s2 = s2, max(s1 + num, s2)
        return s2