# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def maxNode(nums, i, j):
            if i > j:
                return None
            m = i
            for k in range(i, j + 1):
                if nums[k] > nums[m]:
                    m = k
                k += 1
            node = TreeNode(nums[m])
            node.left = maxNode(nums, i, m - 1)
            node.right = maxNode(nums, m + 1, j)
            return node

        return maxNode(nums, 0, len(nums) - 1)
