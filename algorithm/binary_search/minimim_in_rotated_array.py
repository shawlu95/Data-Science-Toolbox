def search(self, nums, target):
    """
    In a rotated ascending array, find the minimum.
    Find the first number that is smaller than the last number nums[-1].
        XXXXXXX....XOOO...O

    Cannot compare to the first number, because the array may not be rotated.
        < nums[0] never finds a match: `XXXXXXXX...X`
        <= nums[0]: get `OXXXXXX....X`
    """
    if not nums: return -1
    l, r = 0, len(nums) - 1

    # compare to last number
    right = lambda x: nums[x] <= nums[-1]

    # exit loop when l, r are consecutive
    while l + 1 < r:
        m = (r - l) // 2 + l

        if right(m):
            r = m
        elif right(m) is False:
            l = m + 1

    if right(r):
        return r
    elif right(l):
        return l
    return -1
