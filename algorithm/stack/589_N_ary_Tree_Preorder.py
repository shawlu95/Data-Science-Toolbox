"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorderStack(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        ans = []

        # edge case: root is None
        if not root: return ans

        stack = [root]
        while stack:
            node = stack.pop()
            ans.append(node.val)

            # node: append child from right to left
            for child in node.children[::-1]:
                stack.append(child)
        return ans

    def preorderRec(self, root):
        """
        Recursion solution
        :type root: Node
        :rtype: List[int]
        """
        ans = []

        # edge case is implicitly handled
        def traverse(node):
            if not node:
                return

            ans.append(node.val)
            for child in node.children:
                traverse(child)

        traverse(root)
        return ans
