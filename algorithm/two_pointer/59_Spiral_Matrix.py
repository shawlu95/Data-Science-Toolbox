class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        A = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in range(n * n):
            A[i][j] = k + 1

            # make a right turn when cell ahead is not zero
            if A[(i + di) % n][(j + dj) % n]:
                di, dj = dj, -di
                # cycle: di, dj
                # 0, 1 move right
                # 1, 0 move down
                # 0, -1 move left
                # -1, 0 move up
            i += di
            j += dj
        return A