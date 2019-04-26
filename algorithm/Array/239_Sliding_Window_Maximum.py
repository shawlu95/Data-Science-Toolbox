def maxSlidingWindow(nums, k):
    ans = []
    queue = []
    for i, v in enumerate(nums):
        # corner case, when front element is outside the window
        if queue and queue[0] == i - k:
            queue.pop(0)

        # pop all elements smaller than new element to be added
        # so after the new element is added, maximum is at queue front
        while queue and nums[queue[-1]] < v:
            queue.pop()
        queue.append(i)

        # when i reaches k - 1, there are k elements in window
        # from now on, append sliding max in every step
        if i + 1 >= k:
            ans.append(nums[queue[0]])
    return ans


maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)