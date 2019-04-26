class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        g = {x: [] for x in range(n)}
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        visited = [False] * n

        ans = 0

        for i in range(n):
            if visited[i] is False:
                queue = [i]
                ans += 1
                while queue:
                    node = queue.pop(0)
                    for nei in g[node]:
                        if visited[nei] is False:
                            visited[nei] = True
                            queue.append(nei)
        return ans

    # alternatively, do not use a list to keep track of visited nodes
    def countComponents2(n, edges):
        g = {x: [] for x in xrange(n)}
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        ret = 0
        for i in range(n):
            queue = [i]
            ret += 1 if i in g else 0
            for j in queue:
                if j in g:
                    queue += g[j]
                    del g[j]

        return ret