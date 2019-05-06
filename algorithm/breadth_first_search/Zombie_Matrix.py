// version 1


class Solution:
    # @param {int[][]} grid  a 2D integer grid
    # @return {int} an integer
    def zombie(self, grid):
        # Write your code here
        n = len(grid)
        if n == 0:
            return 0

        m = len(grid[0])
        if m == 0:
            return 0

        q = []
        for i in xrange(n):
            for j in xrange(m):
                if grid[i][j] == 1:
                    q.append((i, j))

        d = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        days = 0
        while q:
            days += 1
            new_q = []
            for node in q:
                for k in xrange(4):
                    x = node[0] + d[k][0]
                    y = node[1] + d[k][1]
                    if x >= 0 and x < n and y >= 0 and y < m and grid[x][y] == 0:
                        grid[x][y] = 1
                        new_q.append((x, y))
            q = new_q

        for i in xrange(n):
            for j in xrange(m):
                if grid[i][j] == 0:
                    return -1

        return days - 1

// verison 2


class Solution:
    # @param {int[][]} grid  a 2D integer grid
    # @return {int} an integer

    def zombie(self, grid):
        # Write your code here
        sum_zombie = 0
        sum_wall = 0
        n = len(grid)
        m = len(grid[0])
        qzombie = []
        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]

        for i in xrange(n):
            for j in xrange(m):
                if grid[i][j] == 1:
                    qzombie.append([i, j, 0])
                    sum_zombie += 1
                elif grid[i][j] == 2:
                    sum_wall += 1

        step = 0
        while qzombie:
            p = qzombie.pop(0)
            for i in xrange(4):
                x = p[0] + dx[i]
                y = p[1] + dy[i]
                if x < 0 or x >= n or y < 0 or y >= m:
                    continue
                if grid[x][y] == 0:
                    grid[x][y] = 1
                    qzombie.append([x, y, p[2] + 1])
                    sum_zombie += 1
            if not qzombie:
                step = p[2]
        if sum_zombie + sum_wall != n * m:
            return -1
        else:
            return step