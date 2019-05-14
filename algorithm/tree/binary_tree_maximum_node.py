class Solution:
    """
    Leaf node is handled implicitly.
    """
    def maxNode(self, root):
        self.avg = -2 ** 30
        self.node = root
        def traverse(root):
            # write your code here
            if not root:
                return 0, 0

            # if not root.left and not root.right:
            #     return root.val, 1

            l_sum, l_size = traverse(root.left)
            r_sum, r_size = traverse(root.right)
            cur_sum = l_sum + r_sum + root.val
            cur_size = l_size + r_size + 1

            avg = cur_sum / cur_size
            if avg > self.avg:
                # update benchmark
                self.avg = cur_sum / cur_sum
                self.node = root
            return cur_sum, cur_size

        traverse(root)
        return self.node
