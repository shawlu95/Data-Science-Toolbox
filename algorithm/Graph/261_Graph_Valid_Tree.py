from UnionFind import UnionFind
class Solution(object):
    # BFS
    def validTreeBFS(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        dic = {i: set() for i in range(n)}
        for i, j in edges:
            dic[i].add(j)
            dic[j].add(i)
        visited = set()
        queue = [0]
        while queue:
            node = queue.pop(0)
            for neighbor in dic[node]:
                if neighbor in visited:
                    return False

                visited.add(neighbor)
                queue.append(neighbor)
                dic[neighbor].remove(node) # remove an inward edge
            del dic[node] # remove all outward edges at once
        return not dic

    def validTreeBFS2(self, n, edges):
        if len(edges) != n - 1:
            return False

        neighbors = {i: [] for i in range(n)}
        for v, w in edges:
            neighbors[v].append(w)
            neighbors[w].append(v)

        queue = [0]
        for v in queue:
            queue += neighbors.pop(v, [])

        return not neighbors

    # topological sort
    # https://leetcode.com/problems/graph-valid-tree/discuss/69085/A-python-solution-with-topological-sort
    def validTreeTS(self, n, edges):
        graph = {i: set() for i in range(n)}
        for p, q in edges:
            graph[p].add(q)
            graph[q].add(p)
        while graph:
            leaves = []
            for node, neighbors in graph.items():
                if len(neighbors) <= 1:
                    leaves.append(node)
            if len(leaves) == 0:
                return False  # a cycle exists
            for n in leaves:
                if len(graph[n]) == 0:
                    # must be one connected component
                    return len(graph) == 1
                nei = graph[n].pop()
                graph[nei].remove(n)
                del graph[n]
        return True

    # union find
    def validTreeUF(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        parent = [i for i in range(n)]

        # doesn't matter which number to initialize with, it's all relative
        rank = [-1] * n
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            # passed in as root, no need to find root again
            if x == y:
                return

            if rank[x] < rank[y]:
                # no need to adjust rank of y, since adding a small tree to larger tree doesn't change the rank of large tree
                parent[x] = y
            elif rank[x] > rank[y]:
                parent[y] = x
            else:
                parent[x] = y
                rank[y] += 1

        for e in edges:
            # x, y = map(find, e)
            xr = find(e[0])
            yr = find(e[1])
            # if x, y share the same root, cycle exists
            if xr == yr:
                return False
            # parent[xr] = yr
            union(xr, yr)
        return len(edges) == n - 1

    def validTreeUF2(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        # if len(edges) != n - 1:
        #     return False

        uf = UnionFind(n)
        for i, j in edges:
            uf.union(i, j)
        print(uf.parent)
        return uf.group == 1



solver = Solution()
solver.validTreeUF2(5, [[0,1], [1,2], [2,3], [1,3], [1,4]])
# # solver.validTreeUF2(5, [[0,1],[0,2],[0,3],[1,4]])
# solver.validTreeUF2(4, [[2,3],[1,2],[1,3]])