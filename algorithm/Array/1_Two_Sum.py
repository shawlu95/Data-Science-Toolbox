class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        complement = {}

        # note:
        # start with smallest element, guaranteed to be smaller than target
        # because solution is exact unique, the complement will be found

        # corner case
        # 1. empty (not allowed)
        # 2. same elements (duplicate)

        # one-pass solution
        for i, num in enumerate(nums):
            if target - num in complement:
                return [complement[target - num], i]
            else:
                complement[num] = i

        # two-pass solution
        # for i, num in enumerate(nums):
        #     complement[num] = i
        # for i, num in enumerate(nums):
        #     if target - num in complement and complement[target - num] != i:
        #         return [complement[target - num], i]

