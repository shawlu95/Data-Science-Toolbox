from collections import defaultdict

class Solution:
    # @param {int[]} org a permutation of the integers from 1 to n
    # @param {int[][]} seqs a list of sequences
    # @return {boolean} true if it can be reconstructed only one or false
    # Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs
    def sequenceReconstruction(self, org, seqs):
        edges = defaultdict(list)
        indegrees = defaultdict(int)
        nodes = set()
        for seq in seqs:
            nodes |= set(seq) # union of seqs
            for i in range(len(seq)):
                if i == 0:
                    indegrees[seq[i]] += 0
                if i < len(seq) - 1:
                    edges[seq[i]].append(seq[i + 1])
                    indegrees[seq[i + 1]] += 1

        queue = [k for k in indegrees if indegrees[k] == 0]
        res = []

        while len(queue) == 1:
            cur_node = queue.pop()
            res.append(cur_node)
            for node in edges[cur_node]:
                indegrees[node] -= 1
                if indegrees[node] == 0:
                    queue.append(node)
        if len(queue) > 1:
            return False
        return len(res) == len(nodes) and res == org

    def sequenceReconstruction2(self, org, seqs):

        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        edges = defaultdict(set)
        indeg = defaultdict(int)
        nodes = set()

        # build graph, populate edges and indeg
        for seq in seqs:
            # union of nodes, used to check length of reconstructed sequence
            nodes |= set(seq)

            # handle corner case when len(seq) == 1
            # must enter the first iteration (cannot use range(0, len(seq) - 1))
            for i in range(0, len(seq)):
                if i == 0 and seq[i] not in indeg:
                    indeg[seq[i]] = 0

                if i < len(seq) - 1:
                    if seq[i + 1] not in edges[seq[i]]:
                        edges[seq[i]].add(seq[i + 1])
                        indeg[seq[i + 1]] += 1

        # standard topological sort
        queue = [k for k in indeg if indeg[k] == 0]
        res = []

        # when there are more than 1 element in queue, exit loop and return False
        while len(queue) == 1:
            node = queue.pop()
            res.append(node)
            for neighbor in edges[node]:
                indeg[neighbor] -= 1
                if indeg[neighbor] == 0:
                    queue.append(neighbor)
        if len(queue) > 1:
            return False

        return len(res) == len(nodes) and res == org

    # accepted: be aware of reversing order in the end
    def sequenceReconstruction3(self, org, seqs):

        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        out = defaultdict(int)
        ind = defaultdict(set)
        nodes = set()

        # build graph, populate edges and indeg
        for seq in seqs:
            # union of nodes, used to check length of reconstructed sequence
            nodes |= set(seq)

            # handle corner case when len(seq) == 1
            # must enter the first iteration (cannot use range(0, len(seq) - 1))
            for i in range(0, len(seq)):
                # every edge points from i to i + 1
                # append INDEGREE of i + 1
                # increment OUTDEGREE of i
                if seq[i] not in out:
                    out[seq[i]] = 0

                if i + 1 < len(seq) and seq[i] not in ind[seq[i + 1]]:
                    ind[seq[i + 1]].add(seq[i])
                    out[seq[i]] += 1

        print(ind, out)
        # standard topological sort
        queue = [k for k in out if out[k] == 0]
        res = []

        # when there are more than 1 element in queue, exit loop and return False
        while len(queue) == 1:
            node = queue.pop()
            res.append(node)
            for neighbor in ind[node]:
                out[neighbor] -= 1
                if out[neighbor] == 0:
                    queue.append(neighbor)
        if len(queue) > 1:
            return False

        return len(res) == len(nodes) and res == org

solver = Solution()
solver.sequenceReconstruction3([1,2,3], [[1,2],[1,3],[2,3]])
# print(solver.sequenceReconstruction3([4,1,5,2,6,3], [[5,2,6,3],[4,1,5,2]]))