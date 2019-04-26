class Solution:
    def pourWater1(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        #   W
        # | #    |
        # |######|

        for _ in range(V):
            for d in (-1, 1):
                i = low = K
                # less or equal so water can travel
                while 0 <= i + d < len(heights) and heights[i + d] <= heights[i]:
                    # strictly less so water stops traveling
                    if heights[i + d] < heights[i]:
                        low = i + d
                    i += d
                if low != K:
                    heights[low] += 1
                    break
            if low == K:
                heights[K] += 1
        return heights

    def pourWater2(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        for _ in range(V):
            index = K

            for i in range(K - 1, -1, -1):
                if heights[i] > heights[i + 1]:
                    break
                elif heights[i] < heights[i + 1]:
                    index = i

            if index != K:
                heights[index] += 1
                continue

            for i in range(K + 1, len(heights)):
                if heights[i] > heights[i - 1]:
                    break
                elif heights[i] < heights[i - 1]:
                    index = i

            heights[index] += 1

        return heights