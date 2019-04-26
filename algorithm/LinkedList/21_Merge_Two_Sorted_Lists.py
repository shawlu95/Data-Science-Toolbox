# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        p, q, h, s = l1, l2, None, None

        if not p:
            return q
        if not q:
            return p

        if p.val <= q.val:
            s, p = p, p.next
        else:
            s, q = q, q.next

        h = s

        while p and q:
            if p.val <= q.val:
                s.next, s, p = p, p, p.next
            else:
                s.next, s, q = q, q, q.next

        if not p:
            s.next = q
        if not q:
            s.next = p
        return h

    def mergeTwoLists2(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1

        def merge(a, b):
            h = None
            if not a:
                return b
            elif not b:
                return a

            if a.val <= b.val:
                h = a
                h.next = merge(a.next, b)
            else:
                h = b
                h.next = merge(a, b.next)

            return h

        return merge(l1, l2)