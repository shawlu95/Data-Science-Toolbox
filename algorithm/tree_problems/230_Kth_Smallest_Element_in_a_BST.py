import Tree

treeVals = [3,1,4,None,2]
tree = Tree.Tree(treeVals)
root = tree.root

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        arr = []
        def flatten(node, arr):
            if not node:
                return
            flatten(node.left, arr)
            arr.append(node.val)
            flatten(node.right, arr)
        flatten(root, arr)
        return arr[k - 1]

    def kthSmallest2(self, root, k):
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            top = stack.pop()
            print(top.val)
            k -= 1
            if k == 0:
                return top.val
            node = top.right


solver = Solution()
solver.kthSmallest(root, 1)