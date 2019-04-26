
# very bad: do not use
class Solution:
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        # three pointer: i, j, k
        # this solution return unique tuple, not unique set

        # ask clarification
        # can triplet contain duplicate numbers
        # does order matter in triplet

        # if index must be unique, number can be duplicate permutation, then must track index
        # if number cannot be duplicate permutation even though index is unique, okay not to track index, SORT FIRST
        buffer = []
        # nums.sort()
        for i in range(0, len(nums) - 2):
            # find two numbers in [i + 1:] that sum to -a
            a = nums[i]
            cache = {}
            for j in range(i + 1, len(nums)):
                b = nums[j]
                # we want c = - a - b
                cache[- a - b] = j

            for k in range(i + 1, len(nums)):
                c = nums[k]
                if c in cache and cache[c] != k:  # must not reuse same idx
                    buffer.append([a, - a - c, c])  # append [a, b, c]

                    # [a, c, b] also possible
                    # must remove key from dict
                    del cache[- a - c]
        return buffer

arr = [-1, 0, 1, 2, -1, -4]

# return [[-1, 1, 0], [-1, -1, 2], [0, -1, 1]]
# contains two duplicates, but indices are not duplicate
solver = Solution()
print(solver.threeSum(arr))