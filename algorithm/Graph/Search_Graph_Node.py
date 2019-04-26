class Solution:
    def searchNode(self, graph, values, node, target):
        queue = [node]
        visited = set()
        visited.add(node)
        # note: mark ndoe as visited before dequeue
        while queue:
            node = queue.pop(0)
            if values[node] == target:
                return node
            for neighbor in node.neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        return None