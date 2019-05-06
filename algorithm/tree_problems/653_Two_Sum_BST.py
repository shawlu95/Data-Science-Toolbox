# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False
        nums = []

        def inOrder(node, nums):
            if not node:
                return
            inOrder(node.left, nums)
            nums.append(node.val)
            inOrder(node.right, nums)

        inOrder(root, nums)
        print(nums)

        i, j = 0, len(nums) - 1
        while i < j:
            print(i, j)
            if nums[i] + nums[j] == k:
                return True
            elif nums[i] + nums[j] < k:
                i += 1
            elif nums[i] + nums[j] > k:
                j -= 1
        return False

import Tree
treeVals = [0,-1,2,-3,None,None,4]
tree = Tree.Tree(treeVals)
root = tree.root

solver = Solution()
solver.findTarget(root, -4)