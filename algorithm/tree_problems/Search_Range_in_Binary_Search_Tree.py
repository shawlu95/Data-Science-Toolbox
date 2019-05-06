"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    """
    @param root: The root of the binary search tree.
    @param k1 and k2: range k1 to k2.
    @return: Return all keys that k1<=key<=k2 in increasing order.
    """
    # queue method: does not append in sorted order, need to sort before return
    def searchRange1(self, root, k1, k2):
        # write your code here
        ans = []
        if root is None:
            return ans
        queue = [root]
        index = 0
        while index < len(queue):
            if queue[index] is not None:
                if queue[index].val >= k1 and queue[index].val <= k2:
                    ans.append(queue[index].val)

                queue.append(queue[index].left)
                queue.append(queue[index].right)

            index += 1
        return sorted(ans)

    def searchRange2(self, root, k1, k2):
        if k1 > k2:
            return []

        # IMPORTANT: memorize -----------------------
        def searchTarget(root, target):
            if not root:
                return False

            if root.val == target:
                return True
            elif root.val < target:
                return searchTarget(root.right, target)
            else:
                return searchTarget(root.left, target)
        # --------------------------------------------

        res = []

        for target in range(k1, k2 + 1):
            if searchTarget(root, target):
                res.append(target)
        return res