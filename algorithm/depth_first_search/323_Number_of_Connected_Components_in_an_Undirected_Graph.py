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

        def dfs(idx, g, visited):
            if visited[idx]:
                return
            visited[idx] = True
            for nei in g[idx]:
                dfs(nei, g, visited)

        ans = 0
        for i in range(n):
            if visited[i] is False:
                ans += 1
                dfs(i, g, visited)
        return ans

# no need to pass in variable in countComponents stack
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

        def dfs(idx):
            if visited[idx]:
                return
            visited[idx] = True
            for nei in g[idx]:
                dfs(nei)

        ans = 0
        for i in range(n):
            if visited[i] is False:
                ans += 1
                dfs(i)
        return ans
