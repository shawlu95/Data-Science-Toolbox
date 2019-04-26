class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(xy):
            # x, y = map(find, xy)
            x = find(xy[0])
            y = find(xy[1])
            if rank[x] < rank[y]:
                parent[x] = y
            elif rank[x] > rank[y]:
                parent[y] = x
            else:
                parent[y] = x
                rank[x] += 1

        parent, rank = [i for i in range(n)], [0] * n
        # map(union, edges)
        for edge in edges:
            union(edge)
        return len(set([find(x) for x in parent]))

solver = Solution()
solver.countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]])