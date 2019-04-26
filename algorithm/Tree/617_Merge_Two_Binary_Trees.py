import Tree
root_1 = Tree.Tree([1,3,2,5]).root
root_2 = Tree.Tree([2,1,3,None,4,None,7]).root

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2:
            return None
        if not t1:
            return t2
        if not t2:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)

        return t1

    def mergeTreeIterate(self, t1, t2):
        if t1 is None:
            return t2

        stack = [(t1, t2)]
        while stack:
            n1, n2 = stack.pop()

            # if neither exists, nothing to do to
            if not n1 or not n2:
                continue


            n1.val += n2.val

            # if tree 1 is bad, copy from tree 2,
            # regardless of whether tree 2 is bad
            # one tree 1 has a child, it has all
            # descendents of that child from tree 2
            # no need to add anything to queue
            if not n1.right:
                n1.right = n2.right
            else:
                stack.append((n1.right, n2.right))

            if not n1.left:
                n1.left = n2.left
            else:
                stack.append((n1.left, n2.left))

        return t1

    # def mergeTreeIterate2(self, t1, t2):
    #     if t1 is None:
    #         return t2
    #
    #     stack = [[t1, t2]]
    #     while stack:
    #         pair = stack.pop()
    #
    #         n1 = pair[0]
    #         n2 = pair[1]
    #
    #         if not n1 and not n2:
    #             continue
    #
    #         if not n1:
    #             n1 = n2
    #
    #         if n1 and n2:
    #             n1.val += n2.val
    #
    #         # problem: when one node is None, cannot pass None.right to next call
    #         stack.append([n1.right, n2.right])
    #         stack.append([n1.left, n2.left])
    #     return t1

    def mergeTreesBad(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        def merge(t1, t2, parent = None):
            if parent: p = parent.val
            if t1: v1 = t1.val
            if t2: v2 = t2.val

            if not t1 or not t2:
                return

            elif t1 and t2:
                t1.val += t2.val
                merge(t1.left, t2.left, t1)
                merge(t1.right, t2.right, t1)
            elif not t1 and t2:
                parent.right = t2
                merge(None, t2.left, t2)
                merge(None, t2.right, t2)
            elif t1 and not t2:
                merge(t1.left, None, t1)
                merge(t1.right, None, t1)
        merge(t1, t2)
        return t1


solver = Solution()
ans = solver.mergeTreeIterate(root_1, root_2)

tree = Tree.Tree(None)
tree.root = ans
tree.inOrder()