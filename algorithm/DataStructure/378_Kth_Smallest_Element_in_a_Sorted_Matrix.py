class Solution(object):
    # sorting:
    # time O(nlog(n)) where n = RC
    # space O(1)
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        duplicates are counted, e.g. for [1, 2, 2, 3], 3rd smallest is 2, not 3
        """
        flat = [matrix[r][c] for r in range(len(matrix)) for c in range(len(matrix[0]))]
        flat.sort()
        return flat[k - 1]

    # heap
    # time O(log(RC) + 2kLog(R))
    def kthSmallest(self, matrix, k):
        heap = [(row[0], i, 0) for i, row in enumerate(matrix)]
        heapq.heapify(heap)
        ret = 0
        for _ in range(k):
            # if a row has been used up, it will never be pushed into heap again
            ret, r, c = heapq.heappop(heap)
            if c + 1 < len(matrix[0]):
                heapq.heappush(heap, (matrix[r][c + 1], r, c + 1))
        return ret