class Solution(object):
    """
    Use a map to represent a tree, the keys are two digits integers.
    First digit denotes depth. Second digit denotes position.
    Values are the val of tree nodes.

    Key insight is to find depth and position of child nodes.
    """
    # must pass by reference, because it is an integer
    ans = 0

    def pathSum(self, nums):

        # use integer division //
        nodes = {x // 10: x % 10 for x in nums}

        # node is represented by depth(tens) and position(digit)
        def dfs(node, running_sum = 0):
            if node not in nodes:
                return
            running_sum += nodes[node]

            # divmod returns quotient and remainder
            d, p = divmod(node, 10)
            l_child = (d + 1) * 10 + 2 * p - 1
            r_child = (d + 1) * 10 + 2 * p

            # if current node has no child, it is a leaf
            if l_child not in nodes and r_child not in nodes:
                self.ans += running_sum
            else:
                dfs(l_child, running_sum)
                dfs(r_child, running_sum)

        root = nums[0] // 10
        dfs(root)
        return self.ans

solver = Solution()
print(solver.pathSum([113, 215, 221]))