import heapq

class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        nums = [(abs(num - x), num) for num in arr]
        nums.sort(key = lambda pair : [pair[0], pair[1]])
        return sorted([num[1] for num in nums[:k]])

    def findClosestElements2(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        h = [(abs(num - x), num) for num in arr]
        heapq.heapify(h)

        ans = [heapq.heappop(h)[1] for _ in range(k)]
        return sorted(ans)