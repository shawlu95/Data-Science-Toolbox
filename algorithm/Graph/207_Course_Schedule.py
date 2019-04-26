class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
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

        # track number of courses that can be completed
        k = 0
        while dq:
            x = dq.pop(0)
            k += 1
            for i in ind[x]:
                oud[i] -= 1
                if oud[i] == 0:
                    dq.append(i)
        # return true if all courses can be completed
        return k == numCourses

solver = Solution()
# solver.canFinish(8, [[0, 1], [0, 3], [3, 5], [1, 4], [4, 5], [4, 2], [4, 6], [6, 7]])

solver.canFinish(3, [[0, 1], [1, 0], [1, 2]])