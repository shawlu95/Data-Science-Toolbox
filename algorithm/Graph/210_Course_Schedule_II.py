class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        ind = [[] for _ in range(numCourses)]  # indegree
        oud = [0] * numCourses  # outdegree
        for p in prerequisites:
            oud[p[0]] += 1
            ind[p[1]].append(p[0])
        dq = []
        for i in range(numCourses):
            if oud[i] == 0:
                dq.append(i)
        k = 0

        order = []
        while dq:
            x = dq.pop(0)
            order.append(x)
            k += 1
            for i in ind[x]:
                oud[i] -= 1
                if oud[i] == 0:
                    dq.append(i)
        if k == numCourses:
            # order may not be unique, any one is fine
            return order
        return []

solver = Solution()
solver.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])