class Solution:
    def largestNumber(self, nums: 'List[int]') -> 'str':
        def compare(x, y):
            if x + y < y + x:
                return 1
            elif x + y > y + x:
                return -1
            return 0
        # only works in Python2
        strs = list(map(str, nums))
        strs.sort(cmp=compare)
        largest_num = ''.join(strs)
        return largest_num

# python 3
class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x

class Solution:
    def largestNumber(self, nums):
        strs = list(map(str, nums))
        strs.sort(key=LargerNumKey)
        largest_num = ''.join(strs)
        return '0' if largest_num[0] == '0' else largest_num
solver = Solution()
print(solver.largestNumber([3,30,34,5,9]))