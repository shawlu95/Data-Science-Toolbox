class Solution:
    def largestNumber(self, nums):
        strs = [str(num) for num in nums]

        # strs = map(str, nums)

        def compare(x, y):
            if x + y < y + x:
                return 1
            elif x + y > y + x:
                return -1
            return 0

        strs.sort(cmp=compare)
        largest_num = ''.join(strs)
        return '0' if largest_num[0] == '0' else largest_num