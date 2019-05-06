class Solution:
    def sort(self, arr, target):
        nums = [[i, arr[i]] for i in range(len(arr))]
        nums.sort(key = lambda x : x[1])

        for num in nums:
            print(num)

        j = 0
        for i in range(len(nums)):
            while j < len(nums):
                if nums[j][1] - nums[i][1] < target:
                    j += 1
                elif nums[j][1] - nums[i][1] == target:
                    idx = [nums[j][0], nums[i][0]]
                    return [min(idx), max(idx)]
                else:
                    # if difference is greater than target, no need to check larger j
                    # advance i and reset j to i
                    break
        return []

arr = [9, 7, 6, 4, 3, 8]
solver = Solution()
print("ans: ", solver.sort(arr, 2))