class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = pre = ListNode(0)
        dummy.next = cur = head
        while cur and cur.next:
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = cur

            pre.next = tmp

            pre = cur
            cur = cur.next
        return dummy.next