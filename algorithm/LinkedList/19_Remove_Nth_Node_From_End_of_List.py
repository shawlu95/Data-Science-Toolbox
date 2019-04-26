# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head

        # use dummy node to handle special case list = [1] n = 1
        dum = ListNode(0)
        slow, fast = dum, dum
        dum.next = head

        c = 0
        # Advances first pointer so that the gap between first and second is n nodes apart
        while c != n + 1:
            fast = fast.next
            c += 1

        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dum.next


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None

        if head.next == None:
            return head

        pointer = head
        length = 1

        while pointer.next:
            pointer = pointer.next
            length += 1

        rotateTimes = k % length

        if k == 0 or rotateTimes == 0:
            return head

        fastPointer = head
        slowPointer = head

        for a in range(rotateTimes):
            fastPointer = fastPointer.next

        while fastPointer.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next

        temp = slowPointer.next

        slowPointer.next = None
        fastPointer.next = head
        head = temp

        return head