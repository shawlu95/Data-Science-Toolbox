import collections
import string

class Solution(object):

    def findLadders(self, start, end, dic):
        if end not in dic:
            return []

        # faster lookup (time limit exceeded with list)
        dic = set(dic)
        level = {start}

        # maps permuted word to its parent words
        parents = collections.defaultdict(set) # word -> Set[parent words]
        while level and end not in parents:
            next_level = collections.defaultdict(set)

            # compute all words that can be built by modifying on letter
            for node in level:
                for i in range(len(start)):
                    for char in string.ascii_lowercase:
                        n = node[:i] + char + node[i+1:]
                        if n in dic and n not in parents:
                            next_level[n].add(node)
            level = next_level
            parents.update(next_level) # merge dictionaries

        # uses list comprehension to retrieve the path.
        # starting with the endWord and do BFS backward,
        # all valid path will reach the beginWord at the same time.
        res = [[end]]
        while res and res[0][0] != start:
            res = [[p]+r for r in res for p in parents[r[0]]]
        return res

solver = Solution()
solver.findLadders("hit",  "cog", {"hot","dot","dog","lot","log","cog"})
