"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    # stack solution, modified from in-order traversal
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None

        result, stack = [], [(root, False)]
        prev = None
        head = None
        while stack:
            cur, visited = stack.pop()
            if visited:
                if prev:
                    prev.right = cur
                    cur.left = prev
                else:
                    head = cur
                prev = cur
            else:
                if cur.right:
                    stack.append((cur.right, False))
                stack.append((cur, True))
                if cur.left:
                    stack.append((cur.left, False))
        head.left = cur
        cur.right = head
        return head

    # recursive solution
    def treeToDoublyListRec(self, root):

        def helper(curr):
            # if no left child or right child
            head, tail = curr, curr

            # doubly link to left child
            # practice:
            # visualize how it handles
                # leaf nodes
                # immediate parent of leaf (lhead == ltail)
                # ancester with more than two level of subtrees (lhead != ltail != rhead != rtail
            if curr.left:
                lhead, ltail = helper(curr.left)
                ltail.right = curr
                curr.left = ltail
                head = lhead
            if curr.right:
                rhead, rtail = helper(curr.right)
                rhead.left = curr
                curr.right = rhead
                tail = rtail
            return head, tail

        if root:
            head, tail = helper(root)

            # make it circualar
            head.left = tail
            tail.right = head
            return head
        else:
            # corner case
            return None