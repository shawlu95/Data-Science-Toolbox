class UnionFind:
    def __init__(self, N):
        self.group = N                  # all disjoint
        self.parent = list(range(N))    # point to self
        self.rank = [0] * N             # subtree height

    # iterative find
    #        3
    #      6  7
    #          5
    #           8
    # def find(self, p):
    #     parent = self.parent
    #     while p != parent[p]:
    #         parent[p] = parent[parent[p]]
    #         p = parent[p]
    #     return p

    # recursive find (must not use while)
    def find(self, p):
        parent = self.parent
        if p != parent[p]:
            parent[p] = self.find(parent[p])
        return parent[p]

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        i = self.find(p)
        j = self.find(q)
        if i == j:
            return

        # self.parent[i] = j
        # return

        self.group -= 1
        parent, rank = self.parent, self.rank
        if rank[i] < rank[j]:
            parent[i] = j
        elif rank[i] > rank[j]:
            parent[j] = i
        else:
            parent[j] = i
            rank[i] += 1