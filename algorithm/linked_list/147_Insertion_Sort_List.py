class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        dummy = ListNode(0)
        cur = head
        pre = dummy
        while cur:
            nxt = cur.next
            while pre.next and pre.next.val < cur.val:
                pre = pre.next
            cur.next = pre.next
            pre.next = cur
            pre = dummy
            cur = nxt
        return dummy.next

nums = [3, 0, 2, 4, 5]
head = ListNode(nums[0])
pre = head
for i in range(1, len(nums)):
    cur = ListNode(nums[i])
    pre.next = cur
    pre = cur

solver = Solution()
solver.insertionSortList(head)