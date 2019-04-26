# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        level = [root]
        stack = []
        while level:
            stack.append(level)
            nxtLevel = []
            for node in level:
                if node.left:
                    nxtLevel.append(node.left)
                if node.right:
                    nxtLevel.append(node.right)
            level = nxtLevel
        ans = []
        while stack:
            sublist = []
            level = stack.pop()
            for node in level:
                sublist.append(node.val)
            ans.append(sublist)
        return ans

import Tree
treeVals = [3,9,20,None,None,15,7]
root = Tree.Tree(treeVals).root

solver = Solution()
print(solver.levelOrderBottom(root))