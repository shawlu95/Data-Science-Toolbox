class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        n = self.length(head)

        if n < 2:
            return True

        lhead = head  # pointer to the head of the left half
        mid = self.getMiddleLink(head, n)

        if n % 2 != 0:
            mid = mid.next

        rhead = self.reverse(mid)  # pointer to the head of the right half (reversed)

        for _ in xrange(n / 2):
            if lhead.val != rhead.val:
                return False
            lhead, rhead = lhead.next, rhead.next

        return True

    def reverse(self, head):
        if not head:
            return None
        if not head.next:
            return head

        cur = head
        pre = None
        while cur:
            nxt = cur.next
            cur.next = pre
            pre, cur = cur, nxt
        # when loop exits, pre points to the last node, now the new head
        return pre

    def getMiddleLink(self, head, n):
        for _ in xrange(n / 2):
            head = head.next
        return head

    def length(self, head):
        n = 0
        while head is not None:
            head = head.next
            n += 1
        return n