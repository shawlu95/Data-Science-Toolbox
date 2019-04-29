"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        queue = [root]
        depth = 0
        
        while queue:
            depth += 1
            for i in range(len(queue)):
                node = queue.pop(0)
                for child in node.children:
                    queue.append(child)
        return depth