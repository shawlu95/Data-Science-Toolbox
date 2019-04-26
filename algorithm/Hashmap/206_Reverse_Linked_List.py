# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: 'ListNode') -> 'ListNode':
        if not head:
            return

        # pass dummy head as reference to recursion
        dum = ListNode(None)

        def step(cur, dum):
            if cur.next is None:
                dum.next = cur
                return

            step(cur.next, dum)
            cur.next.next = cur
            cur.next = None

        step(head, dum)
        return dum.next