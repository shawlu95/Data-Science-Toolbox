import Tree
import numpy as np

treeVals = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, None, 1]
tree = Tree.Tree(treeVals)
root = tree.root

class Solution(object):
    # 113_Path_Sum_II
    # same as 112 Path Sum, but return path, istead of just true/false
    # be careful to pass copy of list, not reference
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        ans = []
        def rec(node, partial, l, sum):
            """
            In the case where a node has been over extended, do not check if partial sum is equal to sum,
            because the node in previous call may not be a leaf node, it may have another child
            """
            if node is None:
                return
            partial = partial + node.val

            # compare only when current node is a leaf
            if node.left is None and node.right is None and partial == sum:
                ans.append(l + [node.val])

            rec(node.left, partial, l + [node.val], sum)
            rec(node.right, partial, l + [node.val], sum)
        rec(root, 0, [], sum)
        return ans

    def pathSumDFS(self, root, sum1):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        tmp = []

        def find(node):
            if node is None:
                return
            if node.left is None and node.right is None:
                if sum1 == sum(tmp) + node.val:
                    tmp.append(node.val)
                    res.append(list(tuple(tmp)))
                    tmp.pop()
                return

            """
            pattern:
                do something
                recurse
                undo something
            """
            tmp.append(node.val)
            find(node.left)
            tmp.pop()

            tmp.append(node.val)
            find(node.right)
            tmp.pop()

        find(root)
        return res

    # same as above, pass copy instead of reference
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        res = []
        def find(node, tmp):
            if node is None:
                return
            if node.left is None and node.right is None:
                if sum == np.sum(tmp) + node.val:
                    res.append(list(tmp + [node.val]))
                return
            find(node.left, tmp + [node.val])
            find(node.right, tmp + [node.val])

        find(root, [])
        return res

#
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1
solver = Solution()
print(solver.pathSumDFS(root, 22))
