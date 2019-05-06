class SolutionRecursion(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        def traverse(node):
            if not node: return
            ans.append(node.val)
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        return ans

class SolutionStack(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]

        Example
            1
           / \
          2   3
         / \
        1   4

        trace breakpoint:

        cur = 1
        ans = [1]
        stack = [3]

        cur = 2
        and = [1, 2]
        stack = [3, 4]

        cur = 1
        ans = [1, 2, 1]
        stack = [3, 4]

        cur = 4
        ans = [1, 2, 1, 4]
        stack = [3]

        cur = 3
        ans = [1, 2, 1, 4, 3]
        stack = []

        break: stack = [] and cur is None
        """
        stack, ans = [], []
        cur = root
        while cur or stack:
            if not cur:
                cur = stack.pop()
            ans.append(cur.val)

            # visit right child later
            if cur.right:
                stack.append(cur.right)

            # <- break point here
            # visit left child
            cur = cur.left
        return ans

class SolutionStack(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]

        node = 1
        ans = [1]
        stack = [3, 2]

        node = 2
        ans = [1, 2]
        stack = [3, 4, 1]

        node = 1
        ans = [1, 2, 1]
        stack = [3, 4]

        node = 4
        ans = [1, 2, 1, 4]
        stack = [3]

        node = 3
        ans = [1, 2, 1, 4, 3]
        stack = [] -> break
        """
        if not root: eturn []
        stack, ans = [root], []
        while stack:
            node = stack.pop()

            ans.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            # <- breakpoint
        return ans
