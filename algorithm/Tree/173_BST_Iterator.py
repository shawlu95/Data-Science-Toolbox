# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        node = root
        self.stack = []
        while node:
            self.stack.append(node)
            node = node.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0

    def next(self):
        """
        :rtype: int
        """
        smallest = self.stack.pop()

        # if the node that's popped has a right node
        # it means all right children are greater than the popped node and smaller than its parent
        # need to repopulate the stack by left traverssal
        cur = smallest.right
        while cur:
            self.stack.append(cur)
            cur = cur.left
        return smallest.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())