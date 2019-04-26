# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        c = head
        while c:
            n = c
            while n and n.val == c.val:
                tmp = n
                n = n.next
                tmp.next = None
            c.next = n
            c = n
        return head