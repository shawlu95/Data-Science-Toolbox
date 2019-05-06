# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder1(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans, level = [], [root]
        while level:
            ans.append([node.val for node in level])
            temp = []
            for node in level:
                temp.extend([node.left, node.right])
            level = [leaf for leaf in temp if leaf]
        return ans

    def levelOrder2(self, root):
        ans, level = [], [root]
        while root and level:
            ans.append([node.val for node in level])
            LRpair = [(node.left, node.right) for node in level]
            level = [leaf for LR in LRpair for leaf in LR if leaf]
        return ans

    def levelOrder3(self, root):
        ans, level = [], [root]
        while root and level:
            ans.append([node.val for node in level])
            level = [kid for n in level for kid in (n.left, n.right) if kid]
        return ans

    def levelOrder4(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        res, temp, stack = [], [], [root]
        while stack:
            for i in range(len(stack)):
                node = stack.pop(0)
                temp.append(node.val)

                # data structure is modified during iteration!
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
            res.append(temp)
            temp = []
        return res

    def levelOrder5(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        ans = []

        def traverse(node, level, ans):
            if not node:
                return

            curLevel = []
            if level == len(ans):
                ans.append(curLevel)
            else:
                curLevel = ans[level]

            traverse(node.left, level + 1, ans)

            # doesn't matter where to place this line (in/pre/post order)
            curLevel.append(node.val)

            traverse(node.right, level + 1, ans)

        traverse(root, 0, ans)
        return ans