# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head

        # if k is larger than list length, take modulus
        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next
        k = k % count

        if k == 0:
            return head

        # use dummy node to handle special case list = [1] n = 1
        dum = ListNode(0)
        slow, fast = dum, dum
        dum.next = head

        c = 0
        # Advances first pointer so that the gap between first and second is n nodes apart
        while fast and c != k + 1:
            fast = fast.next
            c += 1

        if not fast:
            return head

        while fast:
            slow = slow.next
            fast = fast.next

        # cut list into two
        newHead = slow.next
        slow.next = None

        # traverse to end
        cur = newHead
        while cur.next:
            cur = cur.next

        # move second part to front
        cur.next = dum.next
        dum.next = newHead

        return dum.next