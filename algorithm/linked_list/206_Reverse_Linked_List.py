
class Solution(object):
    #     def reverseList(self, head):
    #         """
    #         :type head: ListNode
    #         :rtype: ListNode
    #         """
    #         if not head:
    #             return None
    #         if not head.next:
    #             return head

    #         cur = head
    #         pre = None
    #         while cur:
    #             nxt = cur.next
    #             cur.next = pre
    #             pre = cur
    #             cur = nxt
    #         return pre

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        def traverse(node):
            current = node
            if node.next == None:
                return node
            newHead = traverse(current.next)

            current.next.next = current

            # must reset, otherwise the first node (old head) will not point to null (cyclic link)
            current.next = None

            return newHead

        return traverse(head)

    def reverseListIter(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head

        cur = head
        pre = None
        while cur:
            nxt = cur.next

            # reverse pointer
            cur.next = pre

            # advance both
            pre, cur = cur, nxt

        # when loop exits, pre points to the last node, now the new head
        return pre

