# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    # BFS
    # key
    #     1. use a dictionary mapping original node to cloned node
    #     2. do not immediately add edge in opposite direction, wait for neighbor to be dequeued
    def cloneGraph(self, node):
        if not node:
            return
        nodeCopy = UndirectedGraphNode(node.label)
        dic = {node: nodeCopy}
        queue = [node]
        while queue:
            # doesn't matter is pop(), or pop(0) BFS
            node = queue.pop(0)
            for neighbor in node.neighbors:
                if neighbor not in dic:
                    # neighbor is not visited
                    neighborCopy = UndirectedGraphNode(neighbor.label)
                    dic[neighbor] = neighborCopy

                    dic[node].neighbors.append(neighborCopy)
                    queue.append(neighbor)
                else:
                    # neighbor has been cloned (adding edge pointing in opposite direction)
                    dic[node].neighbors.append(dic[neighbor])
        return nodeCopy

    # DFS recursive
    def cloneGraphRed(self, node):
        if not node:
            return
        nodeCopy = UndirectedGraphNode(node.label)
        dic = {node: nodeCopy}

        def dfs(node, dic):
            for neighbor in node.neighbors:
                if neighbor not in dic:
                    neighborCopy = UndirectedGraphNode(neighbor.label)
                    dic[neighbor] = neighborCopy
                    dic[node].neighbors.append(neighborCopy)
                    dfs(neighbor, dic)
                else:
                    dic[node].neighbors.append(dic[neighbor])

        dfs(node, dic)
        return nodeCopy

