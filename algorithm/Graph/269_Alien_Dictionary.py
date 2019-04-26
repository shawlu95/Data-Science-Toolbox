class Node(object):
    def __init__(self):
        self.IN = set()
        self.OUT = set()

class Solution(object):
    def alienOrder(self, words):
       # find out nodes
        graph = {}
        for word in words:
            for letter in word:
                if letter not in graph:
                    graph[letter] = Node()

        # WRONG: because directed edge points to letter at same index
        # for word in words:
        #     for i in range(len(word) - 1):
        #         if word[i] != word[i + 1]:
        #             graph[word[i]].OUT.add(word[i + 1])
        #             graph[word[i + 1]].IN.add(word[i])
        # print(graph)

        # find out directed edges (from StefanPochmann)
        for pair in zip(words, words[1:]):
        # loop trough pair 0, 1; 1, 2; 2, 3...
            for a, b in zip(*pair):
            # compare letters at the same index, until end of shorter word
                if a != b:
                    graph[a].OUT.add(b)
                    graph[b].IN.add(a)
                    break
                   # anything beyond the first ordered pair does not imply order

        # topo-sort
        res = ""
        oldlen = len(graph)
        while graph:
            for key in graph:
                if not graph[key].IN:
                    for key2 in graph[key].OUT:
                        graph[key2].IN.remove(key)
                    del graph[key]
                    res += key
                    break

            if oldlen == len(graph): # if shrinking stops, solution doesn't exist
                return ""
            oldlen = len(graph)
        return res

solver = Solution()
print(solver.alienOrder(["wrt","wrf","er","ett","rftt"]))