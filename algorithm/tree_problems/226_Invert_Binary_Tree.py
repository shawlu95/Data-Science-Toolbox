import Tree
treeVals = [4, 2, 7, 1, 3, 6, 9]
tree = Tree.Tree(treeVals)
root = tree.root

class Solution(object):
    # only invert non-null nodes
    def invertTree(self, root):
        cur_level = [root]

        while len(cur_level) != 0:
            nxt_level = []
            for node in cur_level:
                if node.left:
                    nxt_level.append(node.left)
                if node.right:
                    nxt_level.append(node.right)

            i, j = 0, len(nxt_level) - 1
            while j > i:
                nxt_level[i].val, nxt_level[j].val = nxt_level[j].val, nxt_level[i].val
                i += 1
                j -= 1
            cur_level = nxt_level
        return root

    # classic recursion solution
    def invertTreeRecursion(self, root):
        if not root:
            return
        l_tree = self.invertTree2(root.left)
        r_tree = self.invertTree2(root.right)
        root.left = r_tree
        root.right = l_tree
        return root

    # queue solution, every node has its left and right swapped
    # the order of dequeue in the same level does not matter
    def  invertTreeQueue(self, root):
        if not root:
            return

        queue = [root]
        while len(queue) != 0:
            node = queue.pop()
            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root

#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9

solver = Solution()
solver.invertTreeQueue(root)

#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
tree.inOrder()
