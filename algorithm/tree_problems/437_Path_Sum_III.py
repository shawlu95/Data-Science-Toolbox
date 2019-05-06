import Tree
treeVals = [10,5,-3,3,2,None,11,3,-2,None,1]
# treeVals = []
tree = Tree.Tree(treeVals)
root = tree.root

class Solution():
    ans = 0

    def __init__(self):
        self.ans = 0

    # two level recursion
    def pathSumBrute(self, root, s):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int

        Return the number of path that sum to s
        Path does not have to start at root, or terminate at leaf node
        """
        if not root:
            return self.ans

        def dfs(node, bal):
            if not node:
                return

            if bal == node.val:
                self.ans += 1

            # order does not matter, can do left first or right first
            dfs(node.left, bal - node.val)
            dfs(node.right, bal - node.val)

        # traversal order does not matter (pre-order, in-order, post-order)
        # every node starts fresh, with full balance
        self.pathSumBrute(root.left, s)
        self.pathSumBrute(root.right, s)
        dfs(root, s)

        return self.ans

    def pathSumMemo(self, root, target):
        # define global result and path
        self.result = 0

        # cache records how many times (# different paths) we arrive at each possible sum
        # every time a new sum is computed, we find if any sum (in the earlier path of the same branch)
        # differs from current sum by target (8)
        cache = {0: 1}

        def dfs(root, target, currPathSum, cache):
            # exit condition
            if root is None:
                return
                # calculate currPathSum and required oldPathSum

            currPathSum += root.val
            oldPathSum = currPathSum - target
            # update result and cache
            self.result += cache.get(oldPathSum, 0)
            cache[currPathSum] = cache.get(currPathSum, 0) + 1

            # dfs breakdown (pre-order)
            dfs(root.left, target, currPathSum, cache)
            dfs(root.right, target, currPathSum, cache)

            # when reaching a leaf node, trace backward until can move to a different branch,
            # the currPathSum is no longer available, hence remove one.
            cache[currPathSum] -= 1

        # recursive to get result
        dfs(root, target, 0, cache)

        # return result
        return self.result

#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1

solver = Solution()
print(solver.pathSumMemo(root, 8))