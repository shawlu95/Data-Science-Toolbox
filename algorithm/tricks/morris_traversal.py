# for pre-order tree traversal
"""
This approach is based on Morris's article which is intended to optimize
the space complexity. The algorithm does not use additional space for the
computation, and the memory is only used to keep the output. If one prints
the output directly along the computation, the space complexity would be O(1).

Algorithm

Here the idea is to go down from the node to its predecessor, and each
predecessor will be visited twice. For this, go one step left if possible
and then always right till the end. When we visit a leaf (node's predecessor)
first time, it has a zero right child, so we update output and establish
the pseudo link predecessor.right = root to mark the fact the predecessor is
visited. When we visit the same predecessor the second time, it already
points to the current node, thus we remove pseudo link and move right to
the next node.

If the first one step left is impossible, update output and move right
to next node.
"""

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        node, output = root, []
        while node:
            if not node.left:
                output.append(node.val)
                node = node.right
            else:
                predecessor = node.left

                while predecessor.right and predecessor.right is not node:
                    predecessor = predecessor.right

                if not predecessor.right:
                    output.append(node.val)
                    predecessor.right = node
                    node = node.left
                else:
                    predecessor.right = None
                    node = node.right

        return output
